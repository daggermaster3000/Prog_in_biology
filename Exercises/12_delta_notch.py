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
D1 = 0.99
N1 = 1
#cell 2
D2 = 1
N2 = 1
#other parms
a = 0.01
b = 100
k = 2
h = 2

Cell1 = {"delta":[D1], "notch":[N1]}
Cell2 = {"delta":[D2], "notch":[N2]}

for i in range(0,50):
    #for cell 1
    D1_next = ddpdt(N1,D1,b,h)
    N1_next = dndt(D2,a,N1,k)
    #for cell 2
    D2_next = ddpdt(N2,D2,b,h)
    N2_next = dndt(D1,a,N2,k)
    #update the values
    D1 = D1_next
    D2 = D2_next
    N1 = N1_next
    N2 = N2_next
    
    Cell1["delta"].append(D1)
    Cell2["delta"].append(D2)
    Cell1["notch"].append(N1)
    Cell2["notch"].append(N2)

   
time = np.arange(0,51)
print(Cell1["delta"][-1])
fig,axs = plt.subplots(2)
axs[0].plot(time,Cell1["delta"])
axs[0].plot(time,Cell1["notch"])
axs[1].plot(time,Cell2["delta"])
axs[1].plot(time,Cell2["notch"])
    
