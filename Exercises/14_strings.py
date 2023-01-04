# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:04:49 2023

@author: quill
"""
#implemented a way without having to directly check if even or odd
#based on checking if there is one element left after deleting portions
#of the string by 2
s = 'The air is blue'
l = []
r =  range(0,len(s)-1,2)

while len(s)>0:
    if len(s)==1:
        l.append(s[0])
        break
    else:
        l.append(s[0:2])
        s = s[2:]
        
print(l)