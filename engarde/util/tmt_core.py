'''

'''


import re
import json
import pathlib
from   pprint import pprint as pp
import engarde.util.fileutil as fileutil
import engarde.util.strutil as strutil
'''
     'date': '\nApr 29, 2018\n',
     'events': [
         {
             'event_id': '146786',
             'event_name': ['\n',
                            'Y10 Mixed Saber:\n16 Competitors, a NR Event\n\n',
                            '\n'],
             'fencers': [{'club': 'SPARTAK',
                          'fencer_id': '139652',
                          'fencer_name': 'Qiu, Nathan',
                          'place': '1',
                          'rating': 'U',
                          'rating_earned': ''},
'''

def tmt2ser(tmt):
    events  = tmt['events']
    results = []
    for event in events:
        eventId   = int(event['event_id'])
        eventNane = strutil.normEventName(event['event_name'])
        fencers   = event['fencers']
        for fencer in fencers:
            fencerId     = int(fencer['fencer_id'])
            fencerName   = strutil.normName( fencer['fencer_name'] )
            ratingEarned = fencer['rating_earned']
            results.append( {
                'fencer_id': fencerId,
                'fencer_name': fencerName, 'rating_earner': ratingEarned, 'event_id': eventId, 'event_name': eventNane})
    return results

def storeTmtTable(root, fileName, data):
    pass

def tmt_driver(root):
    paths = pathlib.Path(root)
    for path in paths.iterdir():
        print (str(path))

        with open(path) as fd:
            jobj  = json.load(fd)
            tmt   = fileutil.cleanUp( obj=jobj, fctr=fileutil.StrFunctor() )
            ts = tmt2ser(tmt)
            # import pdb; pdb.set_trace()

if __name__ == '__main__':
    root = '/Users/joshuarandoms/dev/engarde/engarde-db/tmt'
    tmt_driver(root)
'''
python engarde/util/tmt_core.py
'''
