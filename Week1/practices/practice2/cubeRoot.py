# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

x = int(input('Enter an integer: '))
ans = 0

while ans**3 < x:
    ans += 1
    
if ans**3 == x:
    print('Cube root of', str(x), 'is', str(ans))
else:
    print(str(x), 'is not a perfect cube')