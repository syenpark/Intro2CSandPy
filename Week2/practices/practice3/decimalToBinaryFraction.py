# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
s = ''

while x*(2**p) % 1:
    print('Remainder = ' + str(x*(2**p) - int(x*(2**p))))
    p += 1

num = int(x*(2**p))

for i in range(p):
    s = str(num % 2) + s
    num //= 2

print('The binary representation of the decimal', x, 'is', '0.' + s)