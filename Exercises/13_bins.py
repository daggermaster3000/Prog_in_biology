# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:46:44 2022

@author: quill
"""

import numpy as np


def bin_me_daddy(a,l=3):
    
    a *= 10
    a = a.astype(int)
    ind = a//2          #bin step size (times 10 compared to consigne)

    print(np.bincount(ind,minlength=l),"\n")



#exercise
#EX1
#a = np.array([0.13,0.4,0.52])
a = np.array([0.3,0.2,0.4,0.1,0.5,0.5,0.7,1.0,0.3,0.3,0.2,0.1,\
      0.8,0.8,0.7,0.6,0.3,0.0,0.1,0.2,0.7,0.4])**2
print("EX1:")    
bin_me_daddy(a)

#EX2
#Use the np.bincount() function to find out by how many cm men are taller than women on average based on the above numbers (give at least two decimal places).
print("EX2:")  
sex = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]) # male: 0; female: 1
height = np.array([1.83, 1.72, 1.61, 1.68, 1.79, 1.75, 1.92, 1.76, 1.66, 1.68, 1.69, 1.61, 1.70, 1.78]) # in meters

no = np.bincount(sex)
print("number in each sex: ",no)
tot = np.bincount(sex,height)
print("total for each group: ",tot)
means = tot/no
print("Mean for each group: ", means)
print("Diff: ",means[0]-means[1])
