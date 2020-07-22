'''

'''


import re
from   pprint import pprint as pp

def normName2(s):
    m = re.match('(\(\d+\))((.+), (.+))( \:)', s)
    if not m:
        print(s)
        raise ValueError('Unknown type of DE line %s' % s)
    last, first =  m.group(3), m.group(4)
    return last, first

def normScore(s):
    m = re.match('(\d+) - (\d+)', s)
    if not m:
        print(s)
        raise ValueError('Unknown type of score line "%s"' % s)
    last, first =  m.group(1), m.group(2)
    return last, first

# def de2ser(de):
#     n       = len(de)
#     results = {}
#     for i in range(n-1):
#         r0 = de[i]['results']
#         r1 = de[i+1]['results']
#         if i == 0:
#             for k in range(int(len(r1)/2)):
#                 winner, score = normName2(r1[k*2]), r1[k*2+1]
#                 player1, player2 = normName2(r0[k*2]), normName2(r0[k*2+1])
#                 # print ('----', i, k, player1, player2, '->', winner, score)
#                 key = (player1, player2)
#                 results[key] = normScore( score )
#         else:
#             for k in range(int(len(r1) / 2)):
#                 player1, player2 = normName2(r0[k*4]), normName2(r0[k*4 + 2])
#                 winner, score = normName2(r1[k*2]), r1[k*2+1]
#                 # print ('----', i, k, player1, player2, '->', winner, score)
#                 key = (player1, player2)
#                 results[key] = normScore( score )
#     pp(results)
#     return results

def exclude(names, curIx):
    return names[:curIx] + names[curIx+1:]

def score2num(score):
    ind, num = score
    return int(num)

# def pool2ser(pools):
#     n = len(pools)
#     results = []
#     for i in range(n):
#         pool     = pools[i]
#         poolNum  = pool['pool_no']
#         fensData = pool['fencers']
#         names    = [fen['name'] for fen in fensData]
#
#         scores = {}
#         for curIx, fen in enumerate(fensData):
#             name = fen['name']
#             pos  = fen['pool_pos']
#             res  = fen['results']
#             # print (curIx, name, res, exclude(names, curIx))
#             opponents = exclude(names, curIx)
#             for opIx, score in enumerate(res):
#                 score = score2num(score)
#                 opp   = opponents[opIx]
#                 key   = tuple(sorted((opp, name)))
#                 if key not in scores:
#                     scores[key] = [0,0]
#                 scores[key][key.index(name)] = score
#         results.append(scores)
#     return results
'''
'''
