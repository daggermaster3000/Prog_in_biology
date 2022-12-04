# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:10:13 2022

@author: quill
"""

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


h = img.imread('C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\hotspring_pattern.jpg')
 
#mean blue value of right boundary
blue_mean_right = np.mean(h[:-1,-1,2])
print(h[-1,:-1,2])
print(blue_mean_right)
#highlight the right side
h[:-1,-200:-1,1] = 0
h[:-1,-200:-1,0] = 0
h[:-1,-200:-1,2] = 255
plt.imshow(h)
plt.show()