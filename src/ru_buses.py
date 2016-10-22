#!/usr/bin/python

import requests


# -- Skill Behaviours --


def get_welcome_response():

    attributes = {}
    card_title = "Welcome to RU NB Buses Skill"
    speech_output = "Welcome to Rutgers New Brunswick Buses."
    reprompt_text = "Please ask for a route prediction"
    end_session = False

    return build_response(attributes, build_speechlet_response(card_title, speech_output, reprompt_text, end_session))


def fetch_bus_arrival_predictions(intent, session):

    session_attributes = {}
    route = intent['slots']['route']['value']
    stop = intent['slots']['stop']['value']

    nextBusUrl = "http://webservices.nextbus.com/service/publicXMLFeed?a=rutgers"

    if route == 'weekend 1':
        route = 'wknd1'
    if stop == 'Livingston plaza':
        stop = 'beck'

    prediction_payload = {
        'command': 'predictions',
        'r': route,
        's': stop
    }

    response = requests.get(nextBusUrl, prediction_payload)
    root = ET.fromstring(response.content)
    arrival_in_mins = int(root.iter('prediction').next().get('minutes'))

    speech_output = "The %s arrives at %s in %d minutes" % (route, stop,  arrival_in_mins)

    return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, None, False))

# -- Response Helpers --


def build_speechlet_response(title, output, reprompt_text, end_session):

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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
