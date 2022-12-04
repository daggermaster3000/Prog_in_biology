# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:54:55 2022

@author: quill
"""


def sum_average(list):
    s = sum(list)
    return(s,s/len(list))

l = [5.75, 5.37, 2.45, 8.22, 7.45, 1.89, 3.82, 2.49]
summe, mean = sum_average(l)
print(int(summe * mean))