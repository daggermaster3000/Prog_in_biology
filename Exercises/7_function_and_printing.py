# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:59:43 2022

@author: quill
"""

def test_square(a, b):
    sq_a = a**2
    
    if sq_a > b:
        print(f'The square of {a} is not smaller than {b}')