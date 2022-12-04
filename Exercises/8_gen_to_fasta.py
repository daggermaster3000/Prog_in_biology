# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:09:11 2022

@author: quill
"""
import os
import numpy as np

def gen_to_fasta(seq_ID):
    path = "C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\" +str(seq_ID)+".genbank.txt"
    new_path = "C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\" +str(seq_ID)+".fasta.txt"
    with open(path) as file:
        data = file.read()
    data = data.partition("ORIGIN")[2]
    data = data.partition("//")[0]
    data = data.split('\n')
    
    
    for i, el in enumerate(data):
        if len(el) == 0:
            del data[i]
            
    for i, el in enumerate(data):
        data[i] = data[i].lstrip('0123456789.- ')
        data[i] = data[i].replace(" ", "")
        data[i] = data[i].upper()
        data[i] = data[i] + "\n"
        
    print(len(data[1]))
    with open(new_path,"w") as new_file:
        new_file.write(">header\n")
    with open(new_path,"a") as new_file:
        for i in data:
            new_file.write(i)
    osCommandString = "notepad.exe " + new_path
    os.system(osCommandString)


def insert_space(string, integer):
    for i in integer:
        string = string[0:i] + ' ' + string[i:]
    return(string)

def fasta_to_gen(seq_ID):
    path = "C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\" +str(seq_ID)+".fasta.txt"
    new_path = "C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\" +str(seq_ID)+".genbank.txt"
    with open(path) as file:
        data = file.readlines()
    data = data[1:]
    line_nb = 1
    for i,el in enumerate(data):
        data[i] = data[i].lower() 
        data[i] = insert_space(data[i],np.arange(5,len(data[i])+6,6))
        data[i] =  '{:7d} {}'.format(line_nb, data[i])
        line_nb += 60

        

    with open(new_path,"w") as new_file:
        new_file.write("<header\nORIGIN\n")
    with open(new_path,"a") as new_file:
        for i in data:
            new_file.write(i)
    osCommandString = "notepad.exe " + new_path
    os.system(osCommandString)
    
#gen_to_fasta("P42677")
fasta_to_gen("Q9NSA3")   