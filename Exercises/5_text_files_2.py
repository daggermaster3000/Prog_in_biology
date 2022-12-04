# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:46:27 2022
This string contains letters, stars and a line ending. Use .strip(), .split() and "".join() (and other functions) in order to find out how many letters the string contains.

How many letters (excluding line ending) does s have?
@author: quill
"""

s = 'dfkfje*jfdn*pwndnv*sfkjadjbvbjbajbfkaj*nkd*nvndlanakndndhnfajnja*lsdkjf*cevgfjh**nfe*en*m\r\n'

s = s.strip()
s = "".join(s)
s = s.split("*")
s = "".join(s)
print(len(s),s)
