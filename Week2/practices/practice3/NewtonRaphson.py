# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
x = float(input('Enter a float number: '))

guess = x/2.0
epsilon = 0.01
num_guesses = 0

while abs(guess**2 - x) >= epsilon:
    guess = guess - (guess**2 - x) / (2*guess)
    num_guesses += 1

print('numGuesses = ' + str(num_guesses))
print('Square root of ' + str(x) + ' is about ' + str(guess))
