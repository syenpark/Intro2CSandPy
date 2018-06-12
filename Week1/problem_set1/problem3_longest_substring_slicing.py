# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

s = str(input('Enter a string: '))

# More Python style to leverage 'slicing'

start = 0
current = ''
longest = ''
previous = ''

for i in range(len(s)):
    if s[i] >= previous:
        current = s[start:i+1]
    else:
        start = i
    
    if len(longest) < len(current):
        longest = current
        
    previous = s[i]
    
print(longest)