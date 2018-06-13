# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
decimal = int(input('Enter an integer number: '))

sign = ''
digits = []
binary = ''

if decimal < 0:
    decimal *= -1
    sign = '-'

while decimal:
    digits.insert(0, str(decimal % 2))
    decimal //= 2
    
print(sign + binary.join(digits))