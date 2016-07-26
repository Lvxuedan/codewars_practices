# -*- coding: utf-8 -*-

'''Candy problem'''
def candies(s):
    if len(s)<=1: return -1
    return len(s) * max(s) - sum(s)
    
print candies([5,8,6,4]) #,9