# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:34:08 2022

@author: quill
"""
import matplotlib.pyplot as plt
import numpy as np

def dndt(D_mean,a,Np,k):
    dnpdt = (D_mean**k/(a+D_mean**k))-Np
    return dnpdt

def ddpdt(Np,Dp,b,h):
    ddpdt = (1/(1+b*Np**h))-Dp
    return ddpdt

#initial parms for cell 1
D1 = 0.5
N1 = 1
#cell 2
D2 = 1
N2 = 1
#other parms
a = 0.01
b = 100
k = 2
h = 2
time = 50
unit = 24*60
timestep = 1000

Cell1 = {"delta":[D1], "notch":[N1]}
Cell2 = {"delta":[D2], "notch":[N2]}

for i in np.arange(0,time*unit,timestep):
    #for cell 1
    D1_next = D1 + ddpdt(N1,D1,b,h)/unit
    N1_next = N1 + dndt(D2,a,N1,k)/unit
    #for cell 2
    D2_next = D2 + ddpdt(N2,D2,b,h)/unit
    N2_next = N2 + dndt(D1,a,N2,k)/unit
    #update the values
    D1 = D1_next
    D2 = D2_next
    N1 = N1_next
    N2 = N2_next
    
    Cell1["delta"].append(D1)
    Cell2["delta"].append(D2)
    Cell1["notch"].append(N1)
    Cell2["notch"].append(N2)

   
time1 = np.arange(0,time*unit+1,timestep)
print(f"Delta final cell 1: {Cell1['delta'][-1]} \n notch final cell 1: {Cell1['notch'][-1]}")
print(f"Delta final cell 2: {Cell2['delta'][-1]} \n notch final cell 2: {Cell2['notch'][-1]}")
fig,axs = plt.subplots(2)
fig.suptitle(f"Timestep: {timestep}")
axs[0].set_title("cell 1")
axs[0].scatter(time1,Cell1["delta"],label="delta")
axs[0].plot(time1,Cell1["notch"],label="notch")
axs[0].legend()
axs[1].set_title("cell 2")
axs[1].plot(time1,Cell2["delta"],label="delta")
axs[1].plot(time1,Cell2["notch"],label="notch")
axs[1].legend()
    
