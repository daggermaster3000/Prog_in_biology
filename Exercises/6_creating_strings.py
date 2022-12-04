# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:16:54 2022

@author: quill
"""

chars = []

s = 'ztvnenejsncejajdncalkjalymmxndjfbfbvsjdlfjbbaldkjfnlaqeqwqwplnnnel'
s2 = ""
ind = [0]

print("len:",len(s))

#initiate indexes
for i in range(1,len(s)):
    if i%2 != 0:
        ind.append(i+i-1)
    if i%2 == 0:
        ind.append(i+i)
#get lower borne        
for i in ind:
    if i <= len(s):
        max = ind.index(i)
        

for i in ind[:max]:
    s2 = s2 + s[i]
    
print("max:",max)
print('index:',ind[max])
print(s2)