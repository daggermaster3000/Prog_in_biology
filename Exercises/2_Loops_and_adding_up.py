# -*- coding: utf-8 -*-
"""
Exercises: loop and adding up
"""
'''EX1
n = 213
j = 0
for i in range(0,n+1):
    j += i
print(j)
'''

n = 226
j = 0
for i in range(0,n+1):
    if i%2 == 0:
        j += i
    else:
        pass
print(j)