# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

s = str(input('Enter a string: '))

current = ''
longest = ''
previous = ''

for c in s:
    if c >= previous:
        current += c
        
        if len(longest) < len(current):
            longest = current
    else:
        current = c
    previous = c
    
print(longest)