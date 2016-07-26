# -*- coding: utf-8 -*-
'''MY ANSWER'''
import copy
import time

def det2(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    # return matrix[0][0]* matrix[1][1]-matrix[1][0]*matrix[0][1]
    count = 0
    SC = 0
    for i in range(len(matrix)):
        a = matrix[0][i]
        b = copy.deepcopy(matrix)
        for j in range(1,len(matrix)):
            del b[j][i]
        b.remove(b[0])

        print a*det2(b)
        
        if i%2 == 0:
            SC += a*det2(b)
        else:
            SC -= a*det2(b)
        print 'SC---', SC
    count += SC 
    print 'count===', count 
    return count
            
  

m  = [[5]]
m1 = [[1,3],[2,5]]
m2 = [[2,5,3],[1,-2,-1],[1,3,4]]
m5 = [  [2,   5,  3,  6,  3],
        [17,  5,  7,  4,  2],
        [7,   8,  5,  3,  2],
        [9,   4, -6,  8,  3],
        [2,  -5,  7,  4,  2]]

print det2(m5)



'''OTHER SMARTER ANSWER 用到分片'''

def determinant(m):
    a = 0
    if len(m) == 1:
        a = m[0][0]
    else:
        for n in xrange(len(m)):
            if (n + 1) % 2 == 0:
                a -= m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
            else:
                a += m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
                
    return a