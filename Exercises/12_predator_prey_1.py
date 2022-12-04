# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:17:30 2022

@author: quill
"""
import matplotlib.pyplot as plt
import numpy as np

N_foxes = 100
N_rabbits = 1000
days = 200*24*60

fox = []
rab = []
for i in range(0,days):
    N2_rabbits = N_rabbits + (N_rabbits*0.05)/(24*60) - (0.0002*N_foxes*N_rabbits)/(24*60)
    N2_foxes = N_foxes - (N_foxes*0.1)/(24*60) + (0.0001*N_foxes*N_rabbits)/(24*60)
    N_rabbits = N2_rabbits
    N_foxes = N2_foxes
    fox.append(N_foxes)
    rab.append(N_rabbits)
    #print(N_foxes)

#print(f'number of rabbits {int(N_rabbits)} and foxes {int(N_foxes)} after {days} days')

time = np.arange(0,days)

fig,axs = plt.subplots(2)
axs[0].plot(time,fox)
axs[0].plot(time,rab)
axs[1].plot(fox,rab)

print(max(fox))