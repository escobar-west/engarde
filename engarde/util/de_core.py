'''

'''

import re
from   pprint import pprint as pp

def normName2(s):
    m = re.match('(\(\d+\))(.+)( \:)', s)
    if not m:
        m = re.match('(.+)-Bye-', s)
        if not m:
            raise ValueError('Unknown type of DE line %s' % s)
        else:
            return 'BYE'
    name = m.group(2)
    return name

def normScore(s):
    m = re.match('(\d+) - (\d+)', s)
    if not m:
        raise ValueError('Unknown type of score line "%s"' % s)
    last, first =  m.group(1), m.group(2)
    return last, first

def toInt(score):
    return int(score[0]), int(score[1])

def de2ser(de):
    n = len(de)
    results = []
    firstInd = []
    for i in range(n-1):
        r0 = de[i]['results']
        r1 = de[i+1]['results']
        if i == 0:
            K = 0
            L = 0
            while 1:
                byes = 0
                player1, player2 = normName2(r0[K]), normName2(r0[K+1])
                byes += int( 'BYE'  == player1 )
                byes += int( 'BYE'  == player2 )
                if byes == 0:
                    winner, score = normName2(r1[L]), r1[L+1]
                    score = toInt( normScore( score ) )
                    results.append( ( player1, player2, score[0], score[1] ) )
                    # print( player1, player2, K, L, score, winner )
                    L += 2
                elif byes == 1:
                    # print( player1, player2, K, L )
                    L += 1
                else:
                    raise ValueError('Byes = %s' % byes )
                firstInd.append(byes)
                K += 2
                if L >= len(r1):
                    break
        elif i == 1:
            K = 0
            L = 0
            M = 0
            while 1:
                offset1 = 2
                player1 = normName2(r0[K])
                if firstInd[L]:
                    offset1 -= 1

                player2 = normName2(r0[K + offset1])
                offset2 = 2

                if firstInd[L+1]:
                    offset2 -= 1

                K += offset1 + offset2

                winner, score = normName2(r1[M]), r1[M + 1]
                score = toInt(normScore(score))
                results.append((player1, player2, score[0], score[1]))
                L += 2
                M += 2
                if L >= len(r1):
                    break
        else:
            # print ('++++++++++++++++++++++++++++++++++++++')
            K = 0
            L = 0
            while 1:
                player1, player2 = normName2(r0[K]), normName2(r0[K + 2])
                K += 4
                winner, score = normName2(r1[L]), r1[L + 1]
                score = toInt(normScore(score))
                results.append((player1, player2, score[0], score[1]))
                # print(player1, player2, K, L, score, winner)
                L += 2

                if L >= len(r1):
                    break
    return results

'''
'''
