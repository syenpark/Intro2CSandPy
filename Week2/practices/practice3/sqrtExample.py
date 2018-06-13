# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
num = int(input('Enter an integer: '))

guess = 0
num_guesses = 0

while guess**2 < num:
    guess += 1
    num_guesses += 1
    
if guess**2 == num:
    print('Square root of', num, 'is', guess)
else:
    print(num, "is not a perfect square")
    
    if num < 0:
        print('Just checking... did you mean', -num, '?')