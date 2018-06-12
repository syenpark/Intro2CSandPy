# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

cube = int(input('Enter an integer: '))

for guess in range(abs(cube) + 1):
    if guess**3 == abs(cube):
        if cube < 0:
            guess *= -1
            
        print('Cube root of', str(cube), 'is', str(guess))
        break
    
if guess**3 != cube:
    print(cube, 'is not a perfect cube')   