# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:31:25 2022

@author: quill
"""

codons = []
bases = ["A","C","T","G"]

for i in bases:
    for j in bases:
        for k in bases:
            if i != j and j != k:
                codons.append(i+j+k)
codons.sort()
print(codons[24])


#ex 2


list = ['f', 'l', 'i', 'c', 'o', 'a', 'q', 'p', 'a', 'o', 'n', 'u', 'w', 'm', 'a', 't', 'b', 'o', 'q', 'w', 'v', 'l', 'z', 'g', 'x', 'o', 'm', 'c', 'c', 'i', 'e', 'r', 'h', 'j', 'o', 'm', 'w', 'p', 'f', 'i', 'z', 'g', 'h', 'q', 'p', 'd', 'e', 'r', 'c', 'g', 'd', 's', 'w', 'k', 'g', 'h', 'r', 'd', 't', 'q', 'd', 's', 'n', 'x', 'k', 'z', 'f', 'z', 'a', 'y', 'b', 'w', 'y', 'h', 'q', 's', 'x', 'c', 'u', 'w', 't', 'x']
base = ['a','t','c','g'] 
list2 = []
for i in list:
        if i in base:
            list2.append(i)
print(list2)