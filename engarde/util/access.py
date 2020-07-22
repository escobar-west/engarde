'''

'''

import os
import engarde.util.data_index as dix
import engarde.util.const as econst

def get( name, indexType ):
    trgtRoot  = econst.getenv('trgtRoot')
    indexRoot = os.path.join(trgtRoot, 'index')

    if indexType == 'IndexMap':
        return dix.IndexMap(indexRoot, name=name)
    if indexType == 'IndexSet':
        return dix.IndexSet(indexRoot, name=name)
    if indexType == 'IndexId':
        return dix.IndexId(indexRoot, name=name)
    if indexType == 'IndexList':
        return dix.IndexList(indexRoot, name=name)

    raise ValueError('Unkown type=%s' % indexType)

def getByDate(engId=None):
    '''get all events by date'''

    dateEventIdSet  = get('dateEventIdSet', 'IndexSet')
    eventIdPoolMap  = get('eventIdPoolMap', 'IndexMap')
    eventIdDelemMap = get('eventIdDelemMap','IndexMap')

    for date in sorted(dateEventIdSet.get().keys()):
        eventIds = dateEventIdSet.get(date)

        for eventId in eventIds:
            if not eventIdPoolMap.exists( eventId ):
                print ('Pool not exists', date, eventId )
                pass
            else:
                pool = eventIdPoolMap.get(eventId)
                yield pool

            if not eventIdDelemMap.exists( eventId ):
                print ('DE not exists', date, eventId )
                pass
            else:
                # print ('Exists', date, eventId )
                delim = eventIdDelemMap.get(eventId)
                yield delim



'''
import imp

import engarde.util.data_index as data_index
imp.reload( data_index )

import engarde.util.access as eua
imp.reload( eua )

imp.reload( data_index )
imp.reload( eua )
dateEventIdSet = eua.get('dateEventIdSet', 'IndexSet')
dateEventIdSet

imp.reload( eua )
eua.getByDate()

eventIdPoolMap = eua.get('eventIdPoolMap', 'IndexMap')

'''
