# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

s = str(input('Enter a string: '))

# According to Google Python Style Guide, 
# a list to add each substring and 
# 'join function' are recommended
# to accumulate  a string within a loop 
# instead of + or += because of running time.

current = []
longest = ''
previous = ''

for c in s:
    if c >= previous:
        current.append(c)
        
        if len(longest) < len(current):
            longest = ''
            longest = longest.join(current)
    else:
        current = [c]
    previous = c
    
print(longest)