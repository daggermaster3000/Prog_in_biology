# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:05:32 2022

@author: quill
"""

N_foxes = 100
N_rabbits = 1000
days = 200*24*60


for i in range(0,days):
    N2_rabbits = N_rabbits + (N_rabbits*0.05)/(24*60) - (0.0002*N_foxes*N_rabbits)/(24*60)
    N2_foxes = N_foxes - (N_foxes*0.1)/(24*60) + (0.0001*N_foxes*N_rabbits)/(24*60)
    N_rabbits = N2_rabbits
    N_foxes = N2_foxes
    #print(N_foxes)

print(f'number of rabbits {int(N_rabbits)} and foxes {int(N_foxes)} after {days} days')