# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:52:24 2022

@author: quill
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from scipy import stats
#get the data

os.chdir("C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Prog_in_biology\\Data\\Out")
directory = os.getcwd()
data = []

for filename in os.listdir(directory):
    with open(filename) as file:
        data.append(file.readlines())

#extract the data
df = []
for i in data:
    for j in i[1:]:
       
        temp = j.rstrip("\n").split(",")
        if float(temp[1])>10 and float(temp[1])<1000:
                temp2 = [float(a) for a in temp]
                df.append(temp2)
  
            
df = np.array(df)  

#plot 1
#plt.plot(df[:,1],df[:,2],".k") 
print(stats.spearmanr(df[:,2],df[:,1]))

#autocheck 1
print("AC 1 (nb nuclei): ", len(df))

#part 2
print("\n************part 2\n")

def bin_me_daddy(a,weights=None,l=3,step=100):
    ind = a//step    #bin step size 
    return np.bincount(ind,weights,minlength=l)

means = np.array(df[:,2])

areas = np.array(df[:,1]).astype(int)

#create if infected or not: 0 not, 1 infected
infected = []
for i in means:
    if i >= 12:  
        infected.append(1)
    if i < 12:
        infected.append(0)

#total per bin
total = bin_me_daddy(areas,weights=None)
print(total)

#infected per bin
inf = bin_me_daddy(areas,infected)
print(inf)

#healthy
heal = total-inf

r = inf/total

print(np.round(r,6))


#advanced part I did completely nimport quoi the exercise is supposed to be on FIJI ,1440x936  divide in 48x52
print("\n********advanced part \n")
x = np.array(df[:,3]).astype(int)
y = np.array(df[:,4]).astype(int)
coord = []
for i,j in zip(x,y):
    coord.append([i,j])
    
binx = np.arange(0,1440,48)
biny = np.arange(0,936,52) 

M = np.zeros((30-1,18-1))

for c in coord:
    for i in range(0,len(binx)-1):
        #check x coord 
        if binx[i] <= c[0] <= binx[i+1]:
            #check y coord
            for j in range(0,len(biny)-1):
                if biny[j] <= c[1] <= biny[j+1]:
                    M[i,j] += 1
squares = []
for i in M:
    for j in M:
        for x in j:
            squares.append(x)  
plt.matshow(M)
plt.title("Sum of the densities of all images")
            
squares = np.array(squares).astype(int)           
    


