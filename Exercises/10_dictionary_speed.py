# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:41:13 2022

@author: quill
"""

import numpy.random as rd
import time


def random_list(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in range(length):
        s = ''
        for j in range(5):
            s += alphabet[rd.randint(0, 24)]
        l.append(s)
    return l

def random_dict_from_list(l):
    d = {}
    for i, el in enumerate(l):
        if el in d:
            d[el].append(i)
        else:
            d[el] = [i]
    return(d)


rd.seed(0)
l1 = random_list(10000)
l2 = random_list(10000)

time1 = time.time()
common = []
for fruit in l1:
    if fruit in l2:
        if fruit not in common:
            common.append(fruit)
time2 = time.time()
print(common)
print('time spent on list part:', time2 - time1)
time1 = time.time()
d1 = random_dict_from_list(l1)
d2 = random_dict_from_list(l2)

common = []
for fruit in d1:
    if fruit in d2:
        if fruit not in common:
            common.append(fruit)
time2 = time.time()
print(common)
print('time spent on dict part:', time2 - time1)
print(d1['oodms'])