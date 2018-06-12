# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

s = str(input('Enter a string: '))

num = 0
pattern = 'bob'

# It does not lead an error in Python 
# to slice outside the bounds of a sequence in pure Python 
# Thus, using only len(s) is fine instead of len(s) - len(pattern)

for i in range(len(s)):
    if s[i:i+len(pattern)] == pattern:
        num += 1

print('Number of times bob occurs is:', num)