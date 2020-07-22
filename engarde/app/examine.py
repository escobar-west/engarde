'''

'''

import os
from   pprint import pprint as pp
import engarde.util.const as econst
import engarde.util.data_index as dix
import engarde.util.access as eaccess

def getix():
    return dict(
        badFencerengFencerIdMap = eaccess.get( 'badFencerengFencerIdMap' ),
        eventIdTmtFileSet       = eaccess.get( 'eventIdTmtFileSet' ),
    )

def dates():
    # get all dates
    dateEventIdSet      = eaccess.get('dateEventIdSet')


def getBadFiles():
    fileNames = []
    b = getix()
    bads = b['badFencerengFencerIdMap']._ix['name2target']
    eventIdTmtFileSet = b['eventIdTmtFileSet']
    for (fencerName, eventId) in bads.keys():
        import pdb; pdb.set_trace()
        fileName = eventIdTmtFileSet.get(eventId)
        fileNames.append(fileName)
    return fileNames

def run():
    fencerIdNameMap = eaccess.get('fencerIdNameMap')
    data = fencerIdNameMap.get()
    pp( data )
    print (len(data))

if __name__ == '__main__':
    run()

'''

Facchine, Jennifer
trgtRoot = '/Users/joshuarandoms/data/engarde-db/results'

python engarde/app/examine.py

'''