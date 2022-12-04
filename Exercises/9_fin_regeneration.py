# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:21:00 2022

@author: quill
"""

import numpy as np 

def txt_file_to_ll(filename):
    path = "C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\"+str(filename)
    #open file
    with open(path) as file:
        data = file.read()

    #split at \n
    data = data.split("\n")
    
    #split at  spaces     
    for i,el in enumerate(data):
        data[i] = data[i].split(" ")
        #delete empty spots
        if len(el) == 0:
            del data[i]
    
    # convert data types
    for i, el in enumerate(data):
        data[i][0] = int(data[i][0])
        data[i][2] = float(data[i][2])
       
  
    #return list of lists
    return(data)


l_before = txt_file_to_ll("bif_before.txt")
l_after = txt_file_to_ll("bif_after.txt")


def ll_to_dic(ll):
    dict = {}
    for l in ll:
        
        dict[l[1]]={}
    fishs = []
    #get the list of all fishes
    for i,el in enumerate(ll):
        if el not in fishs:
            fishs.append(el[0])
    #append the dict of dict if fish and ray in el
    for i,el in enumerate(ll):
        for fish in fishs:
            for ray in dict:
                if fish in el and ray in el:
                    dict[ray][fish] = el[2]
        
    return(dict)



def list_to_array(l,nrows=18,ncols=7):
    #init array
    arr = np.zeros((nrows,ncols))
    for i,el in enumerate(arr):
        arr[i] = np.nan
        
    #add values to array with help of ray_dict
    rays = ray_dictionary()
    for i,el in enumerate(l):
        
        arr[rays[el[1]]][el[0]-1] = el[2]
    return(arr)
    
   


def ray_dictionary():
   rays = {}
   for i in range(9): 
      s = 'D' + str(i+1)
      rays[s] = i 
   for i in range(9):
      s = 'V' + str(9-i)
      rays[s] = i + 9 
   return rays


#What is the ratio in bifurcation distances for ray V3 in fish 5 (give at least 7 decimal digits)?
f_5_b = []
f_5_a = []
for l,res in zip([l_before,l_after],[f_5_b,f_5_a]):
    for d in l:
        if d[0] == 5 and d[1] == "V3":
            res.append(d)
#print(f_5_a[0][2]/f_5_b[0][2])

#Calculate the bifurcation distance ratio (after/before) for V3 in fish 5
d_before = ll_to_dic(l_before)  
d_after = ll_to_dic(l_after)
ratio = d_after["V3"][5]/d_before["V3"][5]


#convert list to array
rays = ray_dictionary()
a_before = list_to_array(l_before)
#print(a_before)
#print(a_before[:,4])
#Calculate the ratio for ray V3 in fish 5.
a_after = list_to_array(l_after)
rays = ray_dictionary()
ratio = a_after[rays["V3"],5-1]/a_before[rays["V3"],5-1]         


#calculations and plotting

r = a_after[:,4]/a_before[:,4]
#print(r)

#mean bifurcation ratios for each rays
mbr = []
ratios = a_after/a_before
for i in range(len(a_after)):
    r = a_after[i,:]/a_before[i,:]
    mbr.append(np.nanmean(r))

#print(np.array(mbr))

#Plotting (jlai fait avec le cul là)

import matplotlib.pyplot as plt


def names_of_rays(rays):
    ray_names = 18*['']
    for ray in rays:
        ray_names[rays[ray]] = ray
    return ray_names

def plotting(ratios, mean_ratios, ray_names):
    plt.figure()
    ax = plt.gca()
    # plot the bifurcation ratios for all the rays for one fish after the other
    for fishindex in range(ratios.shape[0]):
        ax.plot(ratios[fishindex],'.',label = 'fish {:d}'.format(fishindex+1))
    ax.plot(mean_ratios,'k', label = 'mean')
    plt.ylim([0, 1.6])
    plt.legend(['fish 1', 'fish 2', 'fish 3', 'fish 4', 'fish 5', 'fish 6', 'fish 7', 'mean'])
    plt.title('Change in bifurcation distances upon fin regeneration.')
    plt.xlabel('Ray')
    plt.ylabel('Relative change in bifurcation distance')
    ax.set_xticks(range(len(ray_names)))
    ax.set_xticklabels(ray_names)


plotting(ratios,mbr,names_of_rays(rays))

