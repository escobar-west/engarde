'''

'''

import re
from   pprint import pprint as pp
import engarde.util.strutil as strutil

def exclude(names, curIx):
    return names[:curIx] + names[curIx+1:]

def score2num(score):
    ind, num = score
    return int(num)

def pool2ser(pools):
    n = len(pools)
    results = []
    for i in range(n):
        pool     = pools[i]
        poolNum  = pool['pool_no']
        fensData = pool['fencers']
        names    = [fen['name'] for fen in fensData]

        scores = {}
        for curIx, fen in enumerate(fensData):
            name = fen['name']
            pos  = fen['pool_pos']
            res  = fen['results']
            # print (curIx, name, res, exclude(names, curIx))
            opponents = exclude(names, curIx)
            for opIx, score in enumerate(res):
                score = score2num(score)
                opp   = opponents[opIx]
                opp, name = strutil.normName(opp), strutil.normName(name)
                key   = tuple(sorted((opp, name)))
                if key not in scores:
                    scores[key] = [0,0]
                scores[key][key.index(name)] = score
        results.append(scores)
    return results
'''
'''
