# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

x = int(input('Enter an integer: '))
num_type = ''

if x%2:
    num_type = 'Odd'
else:
    num_type = 'Even'
    
print('\n' + num_type + '\nDone with conditional')