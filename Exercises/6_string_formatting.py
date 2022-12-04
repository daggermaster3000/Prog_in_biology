# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:20:31 2022

@author: quill
"""

from numpy import pi
p = int(10**4 * pi)
print('{:07d} is an integer'.format(p))
print('{:011.7f} is a float'.format(pi))
print('{:015.7e} is a float in exp notation'.format(pi))

#Write a program to rewrite a given string, such that the first five characters are uppercase, the next five are lowercase, and so on, and finally the string length is written with a width of 10 characters.

s = "SVfAinhCgLeRloWVdFbrNjcphSijvQejfGDtJSVuwprwVnHAQjmlBWAEdddIbKLsCSsaMXNWszx"
s = [i for i in s]

switch = 1
for i,l in enumerate(s):
    if switch > 10:
        switch = 1
    if switch <=5:
        s[i] = s[i].upper()
    if switch > 5:
        s[i] = s[i].lower()
    switch += 1
        
       
s2 = ""
for i in s:
    s2 += str(i)
print('{}{:10d}'.format(s2,len(s2)))
    



