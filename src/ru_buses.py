#!/usr/bin/python

import yaml
import requests
import xml.etree.ElementTree as ET


# -- Skill Behaviours --


def get_welcome_response():

    attributes = {}
    card_title = "Welcome to RU NB Buses Skill"
    speech_output = "Welcome to Rutgers New Brunswick Buses."
    reprompt_text = "Please ask for a route prediction"
    end_session = False

    return build_response(attributes, build_speechlet_response(card_title, speech_output, reprompt_text, end_session))


def invalid_query_response(r, s):

    attributes = {}
    card_title = "Invalid Query!"
    speech_output = "The %s route does not stop at %s" % (r, s)
    reprompt_text = "Please ask for a valid route prediction"
    end_session = False

    return build_response(attributes, build_speechlet_response(card_title, speech_output, reprompt_text, end_session))


def route_not_running_response(r):

    attributes = {}
    card_title = "The %s Route is not Running!" % r
    speech_output = "It seems like the %s route is currently not running" % r
    reprompt_text = "Please ask for another route prediction"
    end_session = False

    return build_response(attributes, build_speechlet_response(card_title, speech_output, reprompt_text, end_session))


# TODO: List off all places of potential conflict and read them back to user
def resolve_proper_stop():

    # For example, the EE stops at train station twice, (traine & trainn_a)
    #   We would list in app and read aloud very specific cases:
    #   "The EE is arriving at train station northbound in __ mins & southbound in ___ mins"

    attributes = {}
    card_title = "Potentially Ambiguous Query"
    speech_output = ""
    reprompt_text = None
    end_session = False

    return build_response(attributes, build_speechlet_response(card_title, speech_output, reprompt_text, end_session))


def fetch_bus_arrival_predictions(intent, session):

    session_attributes = {}
    r = intent['slots']['route']['value'].lower()
    s = intent['slots']['stop']['value'].lower()

    nextBusUrl = "http://webservices.nextbus.com/service/publicXMLFeed?a=rutgers"

    routes = yaml.safe_load(open('route_names.json', 'r'))
    stops = yaml.safe_load(open('stop_names.json', 'r'))
    route_paths = yaml.safe_load(open('route_paths.json', 'r'))

    r_enc = routes[r]
    s_enc = stops[s]

    r_stops = route_paths[r_enc]
    target_stop = set(s_enc).intersection(set(r_stops))

    if len(target_stop) == 0:
        return invalid_query_response(r, s)
    elif len(target_stop) == 2:
        resolve_proper_stop()

    (target_stop,) = target_stop
    prediction_payload = {
        'command': 'predictions',
        'r': r_enc,
        's': target_stop
    }

    # the following can be shipped off to anoother Function
    #   and used for cases when target_stop is both 1 and 2
    nextbus_response = requests.get(nextBusUrl, prediction_payload)
    root = ET.fromstring(nextbus_response.content)
    try:
        arrival_in_mins = int(root.iter('prediction').next().get('minutes'))
    except StopIteration:
        return route_not_running_response(r)

    speech_output = "The %s arrives at %s in %d minutes" % (r, s,  arrival_in_mins)
    reprompt_text = None
    end_session = False

    return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, end_session))

# -- Response Helpers --


def build_speechlet_response(title, output, reprompt_text, end_session=False):

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': end_session
    }


def build_response(session_attributes, speechlet_response):

    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# -- Event handlers --


def on_session_started(request, session):

    print('on_session_started requestId=%s, sessionId=%s', request['requestId'], session['sessionId'])


def on_session_ended(request, session):

    print('on_session_ended requestId=%s, sessionId=%s', request['requestId'], session['sessionId'])


def on_launch(request, session):

    print('on_launch requestId=%s, sessionId=%s', request['requestId'], session['sessionId'])

    return get_welcome_response()


def on_intent(request, session):

    print('on_intent requestId=%s, sessionId=%s', request['requestId'], session['sessionId'])

    intent = request['intent']
    intent_name = intent['name']

    if intent_name == 'NextArrivalIntent':
        return fetch_bus_arrival_predictions(intent, session)
    else:
        raise ValueError('Invalid Intent')

# -- Handler --


def lambda_handler(event, context):

    session = event['session']
    request = event['request']

    print('event.session.application.applicationId=%s', session['application']['applicationId'])

    if session['new']:
        on_session_started({'requestId': request['requestId']}, session)

    if request['type'] == 'LaunchRequest':
        return on_launch(request, session)
    elif request['type'] == 'IntentRequest':
        return on_intent(request, session)
    elif request['type'] == 'SessionEndedRequest':
        return on_session_ended(request, session)
