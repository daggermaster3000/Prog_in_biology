# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:30:56 2022
COIN TOSS EXERCISE
simulate the tossing of a coin a thousand times and determine the longest sequence of consecutive 1s or 2s.
@author: quill
"""

'''***************WARM UP 1
import numpy.random as rd
rd.seed(5)
nb1 = 0
sum = 0
for n in range(500):
    r = rd.randint(1,3)
    if r == 1:
        nb1 += 1
        print(r,nb1)
        sum += nb1
    else:
        nb1 = 0
        print(r,nb1)
'''

'''***************WARM UP 2
import numpy.random as rd
rd.seed(5)
max = 0
for n in range(500):
    r = rd.randint(1,5000)
    if r > max :
        max = r
print(max)
 '''
 
'''FULL EXERCISE'''   
import numpy.random as rd
rd.seed(4)
nb1=0
nb2=0
max = 0
for n in range(1000):
    r = rd.randint(1,3)
    
    if r == 1:
        nb1 +=1
        nb2 = 0
        
    if r == 2:
        nb2 += 1
        nb1 = 0
    
    if nb1>max:
        max = nb1
    if nb2>max:
        max = nb2
    
        
print(max)