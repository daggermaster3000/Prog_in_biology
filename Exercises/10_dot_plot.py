# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:38:22 2022

@author: quill
"""

import matplotlib.pyplot as plt

def slyce(line, width):
    """returns a dictionary. The keys of the dictionary are strings of 'width' 
    characters and the values are lists with the positions of these strings in 'line'."""
    d = {}
    for i in range(0, len(line)-width+1):
        if line[i:i+width] in d:
            d[line[i:i+width]].append(i)
        else:
            d[line[i:i+width]]=[i]
        
    return(d)
        
"""TEST
line1 = 'My care is loss of care, by old care done'
line2 = 'Your care is gain of care, by new care won'
d = slyce(line1,1)
print(d)
#print(d[" care"])
print(len(d))
"""

def match(line1, line2, width):
    """
    Parameters
    ----------
    line1 : Str
        a sequence to match
    line2 : Str
        another sequence to match
    width : Int
        width of the kernel

    Returns a tuple with two lists. These lists will be the x- and y-values to generate the plot above.
    -------
    Find the common elements of the sliced inputs (rel to the kernel) and returns the position in list1 and in list 2
    """
    spl1 = slyce(line1,width)
    spl2 = slyce(line2,width)
    d= {}
    x = []
    y = []
    commons = [i for i in spl1 if i in spl2]
    
    for common in commons:
        d[common] = [spl1[common],spl2[common]]
        
    for key in d:
        len1 = len(d[key][0])
        len2 = len(d[key][1])
        #check if both sequences have the same number of occurences, if not add 0 to the smallest
        if len1 > len2:
            delta = len1-len2
            for i in range(0,delta):
                d[key][1].append(0)
                
        if len1 < len2:
            delta = len2-len1
            for i in range(0,delta):
                d[key][0].append(0)
          
        for i in d[key][0]:
            for j in d[key][1]:
                x.append(i)
                y.append(j)
    print(d)
    return((x,y))
                
def plot(x, y, lablex, labley, width):
          plt.scatter(x,y)
          plt.xlabel(lablex)
          plt.ylabel(labley)
          plt.title(f'Dot plot with window size {width}')
   
    
line1 = 'My care is loss of care, by old care done'
line2 = 'Your care is gain of care, by new care won'
        
d = slyce(line1,5)
d2 = slyce(line2,5)    
        
        
x,y = match(line1,line2,5)
print(len(x))
print(sum(x),sum(y))
    
plot(x,y,line1,line2,5)     
        
        
        