# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:44:24 2022
Mendel stuff
@author: quill
"""
import numpy as np


def simulate_mendel(result,j):
    
    sim_dom = 0
    men_dom = 5474
    men_rec = 1850
    plantnumber=7324
    for i in range(0,plantnumber): 
        a = np.random.randint(1,5)
        if a != 1:
            sim_dom += 1
    
    
    expected_dom=plantnumber*3/4
    
    
    
    if abs(men_dom-expected_dom) < abs(sim_dom-expected_dom):
         result["mendel_closer"] += 1 
    if abs(men_dom-expected_dom) == abs(sim_dom-expected_dom):
        result["equal"] +=1
    if abs(men_dom-expected_dom) > abs(sim_dom-expected_dom):
        result["simulation_closer"] +=1
        
    print(f"{j/plantnumber} %",end="\r")
    
result ={"mendel_closer":0,"simulation_closer":0,"equal":0}    
for j in range(0,10000):
    simulate_mendel(result,j)
print(result)