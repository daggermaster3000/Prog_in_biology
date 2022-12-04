# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:09:00 2022

@author: quill
"""

import numpy as np
import random as rd
rd.seed(4)
#logo = {1:u"\u2663",2:u"\u2666",3:u"\u2665",4:u"\u2660"}
correct130 = 0
ngames = 10000
threshold = 117
for j in range(ngames):
    correct_guess = 0
    for i in range(400):
        card_to_guess = np.random.randint(1,4)
        card_guess = np.random.randint(1,4)
        if card_to_guess == card_guess:
            correct_guess += 1
    if correct_guess >= threshold:
        correct130 += 1
print(correct130)
print(f'probability of getting at least {threshold} : {1-correct130/ngames}')