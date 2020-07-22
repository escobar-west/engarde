'''
constants
'''
import os


class SpecialNames(object):
    FencerExcluded = 'Fencer Excluded'

_env = {
    'joshuarandoms':     {
        'srcRoot'  : '/Users/joshuarandoms/dev/engarde/engarde-db',
        'trgtRoot' : '/Users/joshuarandoms/data/engarde-db/results',
    }
    'escobar':       {
        'srcRoot'  : '/Users/escobar/Dev/engarde/engarde-db',
        'trgtRoot' : '/Users/escobar/',
    }
}

def getuser():
    return os.getenv('USER')

def getenv(name, tag=None):
    if tag is None:
        tag = getuser()

    return _env[tag][name]
