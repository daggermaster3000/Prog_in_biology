# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:21:17 2022

@author: quill
"""
import os
os.chdir('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Exercises')

from gbio import fetch_genbank,read_genbank
from dotplot import match, plot


prots = ['P00846', 'Q95A26', 'Q9T9W0', 'Q2I3G9', 'Q9TA24']
d_prots = {}

#create a dict with sid as key and seq as value

for prot in prots:
    fetch_genbank(prot)
    org,seq = read_genbank(prot+'.genbank')
    d_prots[prot] = [org,seq]
    
#print(d_prots)


#Compute the dotplot coordinates of P00846 (Human) vs Q95A26 (Orangutan) using subsequences of length 10. If the coordinates are x and y respectively, give sorted(zip(x,y))[44]. You need to enter two integers separated by a space.

x,y = match(d_prots['P00846'][1],d_prots['Q95A26'][1],10)
print(sorted(zip(x,y))[44])

#How many matches of subsequences of 10 a.a. are there between Q9T9W0 (chimpanzee) and Q95A26 (orangutan), i.e. how many dots does the dotplot for these sequences contain?

x,y = match(d_prots['Q9T9W0'][1],d_prots['Q95A26'][1],10)

print(len(x))

#How many matches of subsequences of 10 a.a. are there for all of the 10 different species pairs in total (i.e. what is the total number of dots added up for each of the 10 graphs)?
total = 0

pairs = []
for i in range(1,len(prots)):
    for j in range(0,i):
        pairs.append([prots[i],prots[j]])

for sids in pairs:
    x,y = match(d_prots[sids[0]][1],d_prots[sids[1]][1],3)
    plot(x,y,d_prots[sids[0]][0],d_prots[sids[1]][0],3)
    total += len(x)
print(total)
