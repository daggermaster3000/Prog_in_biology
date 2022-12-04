# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:02:38 2022

@author: quill
In addition to short and long names, 
this dictionary contains dates of birth and dates of death. 
Create, based on this dictionary, a new dictionary with dates 
of death as keys and a list with short name(s) as values.
"""
#PART 1
person = {}

person['darwin'] = ['Charles Darwin',
                    '12 February 1809','19 April 1882']
person['shakespeare'] = ['William Shakespeare',
                    '26 April 1564','23 April 1616']
person['cervantes'] = ['Miguel de Cervantes',
                    '29 September 1547','23 April 1616']
person['lincoln'] = ['Abraham Lincoln',
                    '12 February 1809','15 April 1865']


values = [person[i][2] for i in person]

'''
dates = dict.fromkeys(values,[])
for i in person:
    #print(type(i))
    for j in dates:
        if person[i][2] == j:
            
            if len(dates[j])>0:
                dates[j].append(i)
            else:
                dates[j] = [i]
print(dates)
'''
#PART 2
dates = dict.fromkeys(values,[])
for i in person:
    #print(type(i))
    for j in dates:
        if person[i][2] == j:
            
            if len(dates[j])>0:
                dates[j].append(person[i][0])
            else:
                dates[j] = [person[i][0]]
print(dates)
            

    
  
    