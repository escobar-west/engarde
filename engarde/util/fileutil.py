'''
'''

import os
import json

def scan(root, fctr):
    for dirName in os.listdir(root):
        pass

class StrFunctor(object):
    def clean(self, s):
        return str(''.join(e for e in s if ord(e) < 128))

def cleanUp(obj, fctr):
    '''
    fctr.clean( str ) returns clean str
    '''
    #import pdb; pdb.set_trace()
    if isinstance(obj, dict):
        oobj = {}
        for k,v in obj.items():
            kk  = cleanUp(k, fctr)
            vv  = cleanUp(v, fctr)
            oobj[ kk ] = vv
        return oobj

    if isinstance(obj, tuple):
        oobj = []
        for v in obj:
            vv  = cleanUp(v, fctr)
            oobj.append( vv )
        return tuple( oobj )

    if isinstance(obj, list):
        oobj = []
        for v in obj:
            vv  = cleanUp(v, fctr)
            oobj.append( vv )
        return oobj

    if isinstance(obj, (str,)):
        return fctr.clean(obj)

    if isinstance(obj, (int, float)):
        return obj

    if obj is None:
        return obj

    raise ValueError('Unknown type=%s' % str(type(obj)))

def loadClean(path):
    with open(path) as fd:
        obj = json.load(fd)
        # print obj
        oobj = cleanUp( obj=obj, fctr=StrFunctor() )
    return oobj

'''
python C:\\Users\\ilya\\GenericDocs\\dev\\engarde\\src\\util\\fileutil.py
'''
