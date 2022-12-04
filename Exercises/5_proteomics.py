# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:12:59 2022

@author: quill
"""


import os
os.chdir('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\proteomics')

#2
fyle = open('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\proteomics\\human_brain_proteins.csv','r')
brain = fyle.readlines()
fyle.close()
fyle = open('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\proteomics\\human_plasma_proteins.csv','r')
plasma = fyle.readlines()
fyle.close()


for i,line in enumerate(brain):
    brain[i] = brain[i].split(',')
brain_all = [i[0] for i in brain[1:]]
print(len(brain_all))

for i,line in enumerate(plasma):
    plasma[i] = plasma[i].split(',')
plasma_all = [i[0] for i in plasma[1:]]
print(len(plasma_all))


brain_only = []
plasma_only = []
brain_and_plasma = []
for id in brain_all:
   if id in plasma_all:
       brain_and_plasma.append(id)
   else:
        brain_only.append(id)
        
for id in plasma_all:
    if id not in brain_all:
        plasma_only.append(id)
        
brain_only.sort()
plasma_only.sort()
brain_and_plasma.sort()
print("-------")
print(len(brain_only))
print(brain_only[614])

print(len(plasma_only))
print(plasma_only[614])

    
print(len(brain_and_plasma))
print(brain_and_plasma[614])