# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:01:03 2022
counting codons chapter 3
@author: quill
"""

bases = ['A','T','C','G']
count = 1
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            
            if (b1 == b2 or b2 == b3) and not(b1 == b2 == b3):
                print(count,b1+b2+b3)
                count += 1