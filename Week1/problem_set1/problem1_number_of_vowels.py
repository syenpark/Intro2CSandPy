# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

s = str(input('Enter a string: '))

num = 0

for c in s:
    if c in 'aeiou':
        num += 1    

print('Number of vowels: ', num)  