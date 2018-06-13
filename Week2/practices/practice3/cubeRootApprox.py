# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

guess = 0.0
epsilon = 0.01
num_guesses = 0
cube = int(input('Enter a whole number: '))
increment = float(input('Enter an increment: '))

while guess**3 < cube and (cube - guess**3) > epsilon:
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
    