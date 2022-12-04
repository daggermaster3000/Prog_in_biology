# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:53:10 2022

@author: quill
"""

import os
os.chdir('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data')

#2
fyle = open('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\darwin.txt','r')
lines = fyle.readlines()
fyle.close()
new_lines = []
for i in lines:
    i = "".join(i)
    i = i.strip()
    print(i)
    new_lines.append(i.split(' '))
lengths = []
for line in new_lines:
    lengths.append(len(line[2]))
print(sum(lengths)/len(lengths))