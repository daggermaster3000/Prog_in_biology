# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:30:06 2022

@author: quill
"""
import os
os.chdir('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data')
#1
fyle = open('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\thompson.txt','r')
lines = fyle.readlines()
fyle.close()
text_l = []
for i in lines:
    text_l.append(i)
    
#print(text_l[89][:48])

#2
fyle = open('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\crick.txt','r')
lines = fyle.readlines()
fyle.close()
new_file = open('crick_copy.txt', 'w')
for i in lines:
    new_file.write(i)
    
fyle = open('crick_copy.txt')
l_fyle = fyle.readlines()
print(str(l_fyle).strip("'[]"))
fyle.close()