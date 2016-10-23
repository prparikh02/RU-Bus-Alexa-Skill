# Generate mappings of human-understandable route/stop names to their
#   encoded values.

import json


# Generate mappings of human-understandable route names to their encoded values
# Unique [New Brunswick] Routes:
#   A
#   B
#   C
#   EE
#   F
#   H
#   LX
#   REX B
#   REX L
#   New Brunsquick 1 Shuttle
#   New Brunsquick 2 Shuttle
#   Weekend 1
#   Weekend 2
def generate_route_name_mappings():

    return {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'double e': 'ee',
        'e e': 'ee',
        'f': 'f',
        'h': 'h',
        'l x': 'lx',
        'rex b': 'rexb',
        'r e x b': 'rexb',
        'rex l': 'rexl',
        'r e x l': 'rexl',
        'new brunswick shuttle 1': 'w1',
        'new brunswick 1': 'w1',
        'new brunswick shuttle 2': 'w2',
        'new brunswick 2': 'w2',
        'weekend 1': 'wknd1',
        'weekend 2': 'wknd2'
    }


# Generate mappings of human-understandable stop names to their encoded values
# Unique [New Brunswick] Stops:
#   Allison Road Classrooms
#   Biel Road
#   Bravo Supermarket
#   Buell Apartments
#   Busch Campus Center
#   Busch Suites
#   Cabaret Theatre
#   College Hall
#   Colony House
#   Davidson Hall
#   Food Sciences Building
#   Gibbons
#   Henderson
#   Hill Center
#   Katzenbach
#   Liberty Street
#   Library of Science
#   Lipman Hall
#   Livingston Plaza
#   Livingston Student Center
#   Nursing School
#   Paterson Street
#   Public Safety Building North
#   Public Safety Building South
#   Quads
#   Red Oak Lane
#   Rockoff Hall
#   Rutgers Student Center
#   Science Building
#   Scott Hall
#   Stadium
#   Student Activities Center
#   Train Station
#   Visitor Center
#   Werblin Back Entrance
#   Werblin Main Entrance
#   Zimmerli Arts Museum
def generate_stop_name_mappings():

    return {
        'allison road classrooms': ['allison', 'allison_a'],
        'allison road classroom': ['allison', 'allison_a'],
        'allison road classroom building': ['allison', 'allison_a'],
        'arc': ['allison', 'allison_a'],
        'biel road': 'biel',
        'biel': 'biel',
        'bravo supermarket': 'newstree',
        'bravo': 'newstree',
        'buell apartments': ['buel', 'buells'],
        'buell apartment': ['buel', 'buells'],
        'buell': ['buel', 'buells'],
        'busch campus center': ['busch', 'busch_a'],
        'busch student center': ['busch', 'busch_a'],
        'b c c': ['busch', 'busch_a'],
        'b s c': ['busch', 'busch_a'],
        'busch suites': 'buschse',
        'suites': 'buschse',
        'cabaret theater': 'cabaret',
        'cabaret theatre': 'cabaret',
        'cabaret': 'cabaret',
        'college hall': ['college', 'college_a'],
        'colony house': 'colony',
        'colony': 'colony',
        'davidson hall': 'davidson',
        'davidson': 'davidson',
        'food sciences building': 'foodsci',
        'food science building': 'foodsci',
        'food sciences': 'foodsci',
        'food science': 'foodsci',
        'gibbons': 'gibbons',
        'new gibbons': 'gibbons',
        'henderson': 'henders',
        'hill center': ['hilln', 'hillw'],
        'hill': ['hilln', 'hillw'],
        'katzenbach': 'katzenbach',
        'cat zen back': 'katzenbach',
        'liberty street': 'liberty',
        'library of science': 'libofsci',
        'l s m': 'libofsci',
        'lipman hall': 'lipman',
        'lipman': 'lipman',
        'livingston plaza': 'beck',
        'livi plaza': 'beck',
        'plaza': 'beck',
        'livingston student center': ['livingston', 'livingston_a'],
        'livi student center': ['livingston', 'livingston_a'],
        'nursing school': 'nursscho',
        'paterson street': ['patersons', 'patersonn'],
        'paterson': ['patersons', 'patersonn'],
        'patterson street': ['patersons', 'patersonn'],
        'patterson': ['patersons', 'patersonn'],
        'public safety building north': ['pubsafn', 'pubsafs'],
        'public safety north': ['pubsafn', 'pubsafs'],
        'public safety': ['pubsafn', 'pubsafs'],
        'public safety building south': 'pubsafs',
        'public safety south': 'pubsafs',
        'quads': 'quads',
        'the quads': 'quads',
        'livi quads': 'quads',
        'livingston quads': 'quads',
        'red oak lane': ['redoak', 'redoak_a'],
        'red oak': ['redoak', 'redoak_a'],
        'rockoff hall': ['rockhall', 'rockoff'],
        'rockoff': ['rockhall', 'rockoff'],
        'rock off hall': ['rockhall', 'rockoff'],
        'rock off': ['rockhall', 'rockoff'],
        'rutgers student center': ['rutgerss', 'rutgerss_a'],
        'r s c': ['rutgerss', 'rutgerss_a'],
        'college ave student center': ['rutgerss', 'rutgerss_a'],
        'college avenue student center': ['rutgerss', 'rutgerss_a'],
        'science building': 'science',
        'science buildings': 'science',
        'scott hall': 'scott',
        'stadium': 'stadium_a',
        'stadium lot': 'stadium_a',
        'student activities center': ['stuactcntr', 'stuactcntrn', 'stuactcntrn_2', 'stuactcntrs'],
        'sac': ['stuactcntr', 'stuactcntrn', 'stuactcntrn_2', 'stuactcntrs'],
        'sack': ['stuactcntr', 'stuactcntrn', 'stuactcntrn_2', 'stuactcntrs'],
        'train station': ['traine', 'traine_a', 'trainn', 'trainn_a'],
        'visitor center': 'lot48a',
        'werblin back entrance': 'werblinback',
        'werblin back': 'werblinback',
        'werblin': ['werblinback', 'werblinm'],
        'werblin main entrance': 'werblinm',
        'werblin main': 'werblinm',
        'zimmerli arts museum': ['zimmerli', 'zimmerli_2'],
        'zimmerli museum': ['zimmerli', 'zimmerli_2'],
        'zimmerli': ['zimmerli', 'zimmerli_2'],
        'zimmer lee': ['zimmerli', 'zimmerli_2']
    }


# Generate map of route to list of stops
def generate_route_to_stops_mapping():

    return {
        'a': [
            'scott',
            'stuactcntr',
            'lot48a',
            'stadium_a',
            'werblinback',
            'hillw',
            'science',
            'libofsciw',
            'busche',
            'busch_a',
            'buells',
            'werblinm',
            'rutgerss_a'
        ],
        'b': [
            'quads',
            'werblinback',
            'hillw',
            'science',
            'libofsci',
            'busche',
            'busch_a',
            'beck',
            'livingston_a'
        ],
        'c': [
            'werblinback',
            'hillw',
            'allison',
            'hilln',
            'stadium_a'
        ],
        'ee': [
            'scott',
            'traine',
            'patersons',
            'rockoff',
            'pubsafs',
            'cabaret',
            'redoak_a',
            'lipman',
            'foodsci',
            'biel',
            'henders',
            'katzenbach',
            'gibbons',
            'college_a',
            'pubsafn',
            'liberty',
            'patersonn',
            'trainn_a',
            'zimmerli',
            'stuactcntr',
            'rutgerss_a'
        ],
        'f': [
            'scott',
            'pubsafs',
            'cabaret',
            'redoak',
            'lipman',
            'foodsci',
            'biel',
            'henders',
            'katzenbach',
            'gibbons',
            'college_a',
            'stuactcntr',
            'rutgerss_a'
        ],
        'h': [
            'scott',
            'traine',
            'stuactcntr',
            'werblinm',
            'buel',
            'busch_a',
            'davidson',
            'libofsci',
            'allison',
            'hilln',
            'stadium_a',
            'rutgerss_a'
        ],
        'lx': [
            'quads',
            'rutgerss_a',
            'scott',
            'traine',
            'stuactcntr',
            'beck',
            'livingston_a'
        ],
        'rexb': [
            'lipman',
            'college_a',
            'newstree',
            'hillw',
            'allison_a',
            'hilln',
            'pubsafs',
            'rockhall',
            'cabaret',
            'redoak_a'
        ],
        'rexl': [
            'lipman',
            'college_a',
            'newstree',
            'beck',
            'livingston_a',
            'pubsafs',
            'rockhall',
            'cabaret',
            'redoak_a'
        ],
        'w1': [
            'nursscho',
            'colony',
            'rutgerss_a',
            'scott',
            'traine_a'
        ],
        'w2': [
            'nursscho',
            'trainn',
            'zimmerli',
            'stuactcntr',
            'rutgerss_a',
            'colony',
            'traine_a'
        ],
        'wknd1': [
            'rutgerss',
            'scott',
            'traine',
            'stuactcntr'
            'lot48a',
            'werblinback',
            'hillw',
            'science',
            'libofsciw',
            'buschse',
            'busch',
            'beck',
            'livingston',
            'quads',
            'stuactcntrs',
            'pubsafs',
            'cabaret',
            'redoak',
            'lipman',
            'foodsci',
            'biel',
            'henders',
            'katzenbach',
            'gibbons',
            'college',
            'pubsafn',
            'liberty',
            'patersonn',
            'trainn',
            'zimmerli_2',
            'stuactcntrn_2'
        ],
        'wknd2': [
            'rutgerss',
            'scott',
            'traine',
            'patersons',
            'rockoff',
            'pubsafs',
            'cabaret',
            'redoak',
            'lipman',
            'foodsci',
            'biel',
            'henders',
            'katzenbach',
            'gibbons',
            'college',
            'stuactcntr',
            'beck',
            'livingston',
            'quads',
            'busch',
            'davidson',
            'libofsci',
            'allison',
            'hilln'
        ]
    }


with open('route_names.json', 'w') as f:
    json.dump(generate_route_name_mappings(), f, indent=4, sort_keys=True)

with open('stop_names.json', 'w') as f:
    json.dump(generate_stop_name_mappings(), f, indent=4, sort_keys=True)

with open('route_paths.json', 'w') as f:
    json.dump(generate_route_to_stops_mapping(), f, indent=4, sort_keys=True)
