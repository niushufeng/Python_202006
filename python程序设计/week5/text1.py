# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:55:23 2021

@author: h3cvdiuser
"""

from string import digits
from random import choice

z = ''.join(choice(digits) for i in range(1000))
result = {}
for ch in z:
    result[ch] = result.get(ch,0) + 1
    
for digit , fre in sorted(result.items()):
    print(digit,fre,sep = ':')
