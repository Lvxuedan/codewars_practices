# -*- coding: utf-8 -*-

'''
ABAB = 2
AAAB = 1
BAAA = 4
QUESTION = 24572
BOOKKEEPER = 10743
'''
import math
import time
print time.time()
from collections import Counter
alpha = 'QUESTION'

char = list(alpha)
sorted_chat = sorted(alpha)


count = 0
a = len(char)
for I in char:
    divBy = 1
    for i,j in Counter(sorted_chat).iteritems():
        divBy *= math.factorial(j)
    count += (sorted_chat.index(I) * math.factorial(a - 1))/divBy
    a -= 1
    sorted_chat.remove(I)
print count+1
