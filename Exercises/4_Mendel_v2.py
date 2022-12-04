# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:15:53 2022

@author: quill
"""

import numpy as np

exp_dom = [5474,6022,705,882,428,651,787,372,353,64,71,60,67,72,65]
exp_rec = [1850,2001,224,299,152,207,277,193,166,36,29,40,33,28,35]


def simulate_mendel(result,index,men_dom,men_rec):
    
    sim_dom = 0
    plantnumber=men_dom+men_rec
    
    if index <= 6:
        for i in range(0,plantnumber): 
            a = np.random.randint(1,5)
            if a != 1:
                sim_dom += 1
        expected_dom=plantnumber*3/4
    else:
        for i in range(0,plantnumber): 
            a = np.random.randint(1,4)
            if a != 1:
                sim_dom += 1
        expected_dom=plantnumber*2/3
    
    
    
    
    if abs(men_dom-expected_dom) < abs(sim_dom-expected_dom):
         result["mendel_closer"] += 1 

    if abs(men_dom-expected_dom) > abs(sim_dom-expected_dom):
        result["simulation_closer"] +=1
        
    #print(f"{j/plantnumber} %",end="\r")
    
  
closer_mendel = []
closer_sim = []
for index in range(0,len(exp_dom)): 
    result ={"mendel_closer":0,"simulation_closer":0}     
    for j in range(0,1000):
        simulate_mendel(result,index,exp_dom[index],exp_rec[index])
    print("exp #",index,":",result)
    closer_mendel.append(result["mendel_closer"])
    closer_sim.append(result["simulation_closer"])
print(closer_mendel)
print(closer_sim)
