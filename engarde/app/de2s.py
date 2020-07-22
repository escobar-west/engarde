'''

'''
import os
from   pprint import pprint as pp
import engarde.util.de_core as de_core
import engarde.util.fileutil as fileutil

def run(path):
    oobj = fileutil.loadClean(path)
    pp( oobj )
    de = de_core.de2ser(de=oobj['rounds'])
    pp (de)

if __name__ == '__main__':
    d = '/Users/escobar/Dev/engarde/engarde-db/delim'
    # f = '37163.146786.2.DELIM.json'
    f = '40216.159843.2.DELIM.json'
    path = os.path.join(d,f)
    run(path)

'''
python engarde/app/de2s.py
'''
