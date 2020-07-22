'''

'''
import os
import json
from   pprint import pprint as pp
import engarde.util.pool_core as euc
import engarde.util.fileutil as fileutil

def run(path):
    with open(path) as fd:
        obj = json.load(fd)
        # print( obj )
        oobj = fileutil.cleanUp( obj=obj, fctr=fileutil.StrFunctor() )
        pp( oobj )
        results = euc.pool2ser(pools=oobj['pools'])
        pp(results)

if __name__ == '__main__':
    d = '/Users/joshuarandoms/dev/engarde/engarde-db/pool'
    f = '37163.146787.1.POOL.json'
    path = os.path.join(d,f)
    run(path)

'''
python engarde/app/pool2s.py
'''