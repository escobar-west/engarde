'''

'''

import os
import json
import pandas
import shutil
import argparse
import pathlib
import engarde.util.const as econst
import engarde.util.data_index as dix
import engarde.util.strutil as strutil
import engarde.util.de_core as de_core
import engarde.util.fileutil as fileutil
import engarde.util.tmt_core as tmt_core
import engarde.util.pool_core as pool_core

from   engarde.util.exception import BadData

'''
TMT:
    {
        'fencer_id': 114302, 
        'fencer_name': 'Tarbuck, Gabriel', 
        'rating_earner': '', 
        'event_id': 151587, 
        'event_name': 
        'C & Under Senior Mixed Epee:7 Competitors, a E1 Event'
    }
'''

def driverTmt(srcRoot, trgtRoot):
    indexRoot           = os.path.join(trgtRoot, 'index')
    dateEventIdSet      = dix.IndexSet (indexRoot, name='dateEventIdSet', unique=True, keyType=int)
    processedFileList   = dix.IndexList(indexRoot, name='tmt_processedFileList', unique=True)
    fencerId2EventIdList= dix.IndexList(indexRoot, name='fencerId2eventId', unique=True, keyType=int)
    eventIdNameMap      = dix.IndexMap (indexRoot, name='eventIdNameMap', keyType=int)
    fencerIdNameMap     = dix.IndexMap (indexRoot, name='fencerIdNameMap', keyType=int)
    engFencerIdfencerId = dix.IndexId  (indexRoot, name='engFencerIdfencerId',)
    fencerNameEventIdMap= dix.IndexMap (indexRoot, name='fencerNameEventIdMap', keyType=str)
    eventIdTmtFileSet   = dix.IndexSet (indexRoot, name='eventIdTmtFileSet', keyType=int)

    tmtRoot  = os.path.join(srcRoot, 'tmt')
    paths    = pathlib.Path(tmtRoot)

    for path in paths.iterdir():
        path = str(path)

        if processedFileList.exists(name='tmt', val=path):
            print ('driverTmt', 'already processed', path)
            continue

        print('driverTmt', 'processing', path)

        with open(path) as fd:
            jobj    = json.load(fd)
            tmt     = fileutil.cleanUp( obj=jobj, fctr=fileutil.StrFunctor() )
            date    = strutil.normDate3(tmt['date'])
            ts      = tmt_core.tmt2ser(tmt)
            for event in ts:
                fencerId   = event['fencer_id']
                eventId    = event['event_id']
                fencerName = event['fencer_name']
                eventName  = event['event_name']

                if not dateEventIdSet.exists(date, eventId):
                    dateEventIdSet.add(date, eventId)

                if fencerName == econst.SpecialNames.FencerExcluded:
                    print ('driverTmt: skipping %s', str(event))
                    continue
                try:
                    fencerIdNameMap.add(name=fencerId, target=fencerName)
                    fencerId2EventIdList.add(name=fencerId, val=eventId)
                    eventIdNameMap.add(name=eventId, target=eventName)
                    engId = engFencerIdfencerId.add(fencerId)
                    fencerNameEventIdMap.add((fencerName, eventId), engId)
                    eventIdTmtFileSet.add(eventId, path)
                except KeyError as e:
                    raise BadData({'path': path})

        processedFileList.add(name='tmt', val=path)

'''
res = [{('Nakagawa, Sean', 'Qiu, Nathan'): [3, 5],
  ('Swords, Evan', 'Thomas, Devin'): [5, 2],
  ('Swords, Evan', 'Trayanov, David'): [5, 0],
  ('Tann, Justin', 'Thomas, Devin'): [5, 0],
  ('Tann, Justin', 'Trayanov, David'): [5, 0],
  ('Thomas, Devin', 'Trayanov, David'): [5, 0]},
 {('Lira, Daine', 'Nieto, Titus'): [5, 3],
  ('Nieto, Titus', 'Sheres, Asher'): [5, 1],
  ('Patil, Aaryan', 'Popovich, Elizabeth'): [5, 4],
  ('Patil, Aaryan', 'Sheres, Asher'): [5, 2],
  ('Popovich, Elizabeth', 'Sheres, Asher'): [3, 5]}]
'''

def updateFencerNameEventId(keys, fencerNameEventIdMap, engFencerIdfencerId, badFencerengFencerIdMap):
    for key in keys:
        (fencerName, eventId) = key
        if not fencerNameEventIdMap.exists( key, typeCheck=False ):
            engId = engFencerIdfencerId.add( key )
            badFencerengFencerIdMap.add( key, engId )
            fencerNameEventIdMap.add( key, engId )

def driverPool(srcRoot, trgtRoot):
    indexRoot               = os.path.join(trgtRoot, 'index')

    processedFileList       = dix.IndexList(indexRoot, name='pool_processedFileList', unique=True)
    fencerNameEventIdMap    = dix.IndexMap (indexRoot, name='fencerNameEventIdMap' )
    engFencerIdfencerId     = dix.IndexId  (indexRoot, name='engFencerIdfencerId' )
    badFencerengFencerIdMap = dix.IndexMap (indexRoot, name='badFencerengFencerIdMap', unique=True )

    engIdEventIdSet         = dix.IndexSet (indexRoot, name='engIdEventIdSet', unique=True, keyType=int)
    eventIdPoolMap          = dix.IndexMap (indexRoot, name='eventIdPoolMap', unique=True, hasinvet=False, keyType=int)

    poolRoot = os.path.join(srcRoot, 'pool')
    paths = pathlib.Path(poolRoot)

    for path in paths.iterdir():
        path = str(path)

        if processedFileList.exists(name='pool', val=path):
            print ('driverPool', 'already processed', path)
            continue

        print('driverPool', 'processing', path)

        with open(path) as fd:
            jobj    = json.load(fd)
            obj     = fileutil.cleanUp( obj=jobj, fctr=fileutil.StrFunctor() )
            eventId = int(obj['event_id'])
            pools   = obj['pools']
            pools   = pool_core.pool2ser( pools )

            mat     = {'fencer1': [], 'fencer2': [], 'score1':[], 'score2':[] }

            for event in pools:
                for k,v in event.items():
                    fencer1, fencer2 = k
                    score1, score2 = v
                    try:
                        key1 = (fencer1, eventId)
                        key2 = (fencer2, eventId)
                        updateFencerNameEventId( keys                    = [key1, key2],
                                                 fencerNameEventIdMap    = fencerNameEventIdMap,
                                                 engFencerIdfencerId     = engFencerIdfencerId,
                                                 badFencerengFencerIdMap = badFencerengFencerIdMap)

                        fencer1 = fencerNameEventIdMap.get(key1)
                        fencer2 = fencerNameEventIdMap.get(key2)

                        if not engIdEventIdSet.exists(fencer1, eventId):
                            engIdEventIdSet.add(fencer1, eventId)
                        if not engIdEventIdSet.exists(fencer2, eventId):
                            engIdEventIdSet.add(fencer2, eventId)

                    except KeyError as e:
                        raise BadData({'path': path})

                    # print (fencer1, fencer2, score1, score2)
                    mat[ 'fencer1' ].append(fencer1)
                    mat[ 'fencer2' ].append(fencer2)
                    mat[ 'score1'  ].append(score1)
                    mat[ 'score2'  ].append(score2)

            df = pandas.DataFrame(mat)

            if eventIdPoolMap.exists( eventId ):
                dfp = eventIdPoolMap.get( eventId )
                df  = dfp.append( df )
                df  = df.reset_index()
                eventIdPoolMap.reset( eventId, df )
            else:
                eventIdPoolMap.add( eventId, df )

        processedFileList.add(name='pool', val=path)


def driverDelim(srcRoot, trgtRoot):
    indexRoot               = os.path.join(trgtRoot, 'index')

    processedFileList       = dix.IndexList(indexRoot, name='de_processedFileList', unique=True)
    fencerNameEventIdMap    = dix.IndexMap (indexRoot, name='fencerNameEventIdMap' )
    engFencerIdfencerId     = dix.IndexId  (indexRoot, name='engFencerIdfencerId' )
    badFencerengFencerIdMap = dix.IndexMap (indexRoot, name='badFencerengFencerIdMap', unique=True )

    engIdEventIdSet         = dix.IndexSet (indexRoot, name='engIdEventIdSet', unique=True, keyType=int)
    eventIdDelemMap         = dix.IndexMap (indexRoot, name='eventIdDelemMap', unique=True, hasinvet=False, keyType=int)

    delimRoot = os.path.join(srcRoot, 'delim')
    paths = pathlib.Path(delimRoot)

    for path in paths.iterdir():
        path = str(path)

        if processedFileList.exists(name='delim', val=path):
            print ('driverDelim', 'already processed', path)
            continue

        print('driverDelim', 'processing', path)

        with open(path) as fd:
            jobj    = json.load(fd)
            obj     = fileutil.cleanUp( obj=jobj, fctr=fileutil.StrFunctor() )

            eventId = int(obj['event_id'])
            des     = de_core.de2ser(de=obj['rounds'])

            mat     = {'fencer1': [], 'fencer2': [], 'score1':[], 'score2':[] }

            for (fencer1, fencer2, score1, score2) in des:
                try:
                    key1 = (fencer1, eventId)
                    key2 = (fencer2, eventId)
                    updateFencerNameEventId( keys                    = [key1, key2],
                                             fencerNameEventIdMap    = fencerNameEventIdMap,
                                             engFencerIdfencerId     = engFencerIdfencerId,
                                             badFencerengFencerIdMap = badFencerengFencerIdMap)

                    fencer1 = fencerNameEventIdMap.get(key1)
                    fencer2 = fencerNameEventIdMap.get(key2)

                    if not engIdEventIdSet.exists(fencer1, eventId):
                        engIdEventIdSet.add(fencer1, eventId)
                    if not engIdEventIdSet.exists(fencer2, eventId):
                        engIdEventIdSet.add(fencer2, eventId)

                except KeyError as e:
                    raise BadData({'path': path})

                # print (fencer1, fencer2, score1, score2)
                mat[ 'fencer1' ].append(fencer1)
                mat[ 'fencer2' ].append(fencer2)
                mat[ 'score1'  ].append(score1)
                mat[ 'score2'  ].append(score2)

            df = pandas.DataFrame(mat)

            if eventIdDelemMap.exists( eventId ):
                dfp = eventIdDelemMap.get( eventId )
                df  = dfp.append( df )
                df  = df.reset_index()
                eventIdDelemMap.reset( eventId, df )
            else:
                eventIdDelemMap.add( eventId, df )

        processedFileList.add(name='delim', val=path)

def runSteps(step, srcRoot, trgtRoot):
    ''' run steps '''
    if step == 0:
        if os.path.exists(trgtRoot):
            print ('removing', trgtRoot)
            shutil.rmtree(trgtRoot)
    if step == 1:
        driverTmt(srcRoot=srcRoot, trgtRoot=trgtRoot)
    if step == 2:
        driverPool(srcRoot=srcRoot, trgtRoot=trgtRoot)
    if step == 3:
        driverDelim(srcRoot=srcRoot, trgtRoot=trgtRoot)

if __name__ == '__main__':
    parser  = argparse.ArgumentParser(description='egarde')
    parser.add_argument('--step', type=int,  help='step number')
    args    = parser.parse_args()
    step    = args.step

    srcRoot = econst.getenv('srcRoot')
    trgtRoot= econst.getenv('trgtRoot')

    runSteps(step=step, srcRoot=srcRoot, trgtRoot=trgtRoot)



'''
srcRoot = '/Users/joshuarandoms/dev/engarde/engarde-db'
trgtRoot= '/Users/joshuarandoms/data/engarde-db/results'

python engarde/driver/engine.py
'''