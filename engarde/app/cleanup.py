'''

'''
import os
import json
from   pprint import pprint as pp
import engarde.util.fileutil as fileutil

def run(path):
    with open(path) as fd:
        obj = json.load(fd)
        # print obj
        oobj = fileutil.cleanUp( obj=obj, fctr=fileutil.StrFunctor() )
        pp( oobj )

if __name__ == '__main__':
    d = r'C:\Users\ilya\GenericDocs\dev\engarde\engarde-db\delim'
    f = '37163.146786.2.DELIM.json'
    path = os.path.join(d,f)
    run(path)

'''
python engarde\\app\\cleanup.py
'''