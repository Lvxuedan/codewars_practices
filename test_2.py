# -*- coding: utf-8 -*-
import time

def doubles(maxk, maxn):
    print maxk, maxn
    return sum([1.0/(k*(n**(2*k))) for n in range(2,maxn+2) for k in range(1,maxk+1) if k*(n**(2*k))<(10000**90)] )

print time.time()
print doubles(1, 10)    #, 0.5580321939764581)
print doubles(10, 1000) #, 0.6921486500921933)
print doubles(10, 10000)#, 0.6930471674194457)
print doubles(20, 10000)#, 0.6930471955575918)
print time.time()

