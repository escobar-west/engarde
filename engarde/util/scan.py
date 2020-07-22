'''

'''

import pathlib

def driver(poolRoot, deRoot):
    # scan POOL data first
    paths = pathlib.Path(poolRoot)
    for path in paths.iterdir():
        print (str(path))


'''
/Users/joshuarandoms/dev/engarde/engarde-db/pool/38740.154042.1.POOL.json

/Users/joshuarandoms/dev/engarde/engarde-db/pool/38740.154042.1.POOL.json

d = '/Users/joshuarandoms/dev/engarde/engarde-db/pool/'
from pathlib import Path
p = Path(d)
[x for x in p.iterdir() if x.is_dir()]

import engarde.util.scan as pus


'''