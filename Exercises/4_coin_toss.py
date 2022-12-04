# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:46:40 2022
Previously you had to simulate the tossing of a coin a thousand times and determine the longest sequence of consecutive 1s or 2s. Modify this code to find out how many coin tosses are necessary to encounter a sequence of at least eight 1s or 2s for the first time. Since you don't know how often you will have to simulate the tossing, you should use a while-loop. Please simulate the tossing as you did before, but using the following seed:
@author: quill
"""

import numpy.random as rd
rd.seed(0)
nb1=0
nb2=0
max = 0
count = 0
while (max<8):
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
    count+=1
        
print("nb of tosses: ",count)