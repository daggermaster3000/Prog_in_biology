# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:11:29 2022

@author: quill
"""
import numpy.random as rd
rd.seed(141)

higher10 = 0
for j in range(1000):
    count = 0
    for n in range(30):
        r = rd.randint(1,7)
        if r == 6:
            count +=1
        #print(r)
    print(f'times 6: {count}')
    if count >= 10:
        higher10 += 1
print(f'higher than 10: {higher10}')
