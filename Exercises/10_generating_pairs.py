# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:57:12 2022

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



l = ['ball', 'clock', 'glass', 'table']
l = random_list(100)
pairs = []
time1 = time.time()
for word1 in l:
    for word2 in l:
        if word1 != word2 and ([word1,word2] not in pairs) and  ([word2,word1] not in pairs):
            pairs.append([word1,word2])
#print(pairs)
time2 = time.time()
print("time for algo 1:",time2-time1)

#option 2 which is way faster
pairs2 = []
time1 = time.time()
for i in range(1,len(l)):
   
    for j in range(0,i):
        
        pairs2.append([l[i],l[j]])
time2 = time.time()
print("time for algo 2:",time2-time1)       
#print(pairs2)