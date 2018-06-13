# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
cube = int(input('Enter a whole number: '))

low  = 0.0
high = cube
epsilon = 0.01
num_guesses = 0

def func(x):
    return x**3 - cube

while True:
    guess = (low + high) / 2.0
    
    if func(guess) == 0 or ((high - low) / 2.0) < epsilon:
        print('num_guesses =', num_guesses)
        print(guess, 'is close to the cube root of', cube)
        break
    
    if func(guess) * func(low) > 0:
        low = guess
    else: 
        high = guess
        
    num_guesses += 1
    
print('Fail')
