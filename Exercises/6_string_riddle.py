# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:46:38 2022

@author: quill
"""
import urllib.request
file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
message = str(file.read())
print(type(message))

parts = message.partition("mess below:")

msg=[]
for ind,char in enumerate(parts[2]):
    msg.append(char)

#unique characters    
chars = dict.fromkeys(msg)

#count each
for char in chars:
    chars[char] = 0
    for i in msg:
        if i == char:
            chars[char] += 1

for i in chars:
    if chars[i]<10:
        print(i,chars[i])