'''

'''
import os
import json
from   pprint import pprint as pp
import engarde.util.fileutil as fileutil
import engarde.util.tmt_core as tmt_core

def run(path):
    with open(path) as fd:
        obj = json.load(fd)
        # print( obj )
        oobj = fileutil.cleanUp( obj=obj, fctr=fileutil.StrFunctor() )
        pp( oobj )
        pp( tmt_core.tmt2ser(oobj) )

if __name__ == '__main__':
    d = '/Users/joshuarandoms/dev/engarde/engarde-db/tmt'
    f = '37163.TMT.json'
    path = os.path.join(d,f)
    run(path)

'''
python engarde/app/tmt2s.py
'''