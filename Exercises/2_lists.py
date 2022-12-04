# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 20:48:14 2022

@author: quill
"""
lys1 = [7, 3, 2, 5, 1, 4, 4, 6, 2, 9, 1, 6, 3, 2, 6, 5, 5]
lys2 = [8, 9, 8, 9, 6, 4, 5, 5, 8, 2, 4, 3, 1, 6, 5, 6, 5]
lys3 = []
for i in range(0,len(lys1)-1):
    lys3.append(lys1[i]*lys2[i+1])
print(lys3)  
print(sum(lys3))