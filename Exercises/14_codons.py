# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:22:17 2023

@author: quill
"""
#simple answer couldve gotten a bit more creative with the algo
bases = ['A','T','G','C']
codons = []
for i in bases:
    for j in bases:
        for k in bases:
            if (i == j or i == k or j == k) and (i != j or i != k or j != k ):
                codons.append(i+j+k)
codons.sort
print(codons[22])