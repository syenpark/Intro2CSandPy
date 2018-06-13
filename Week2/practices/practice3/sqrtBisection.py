# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
num = int(input('Enter an whole number: '))

low = 0
high = num
guess = 0.0
epsilon = 0.01
num_guesses = 0


def quad_func(x, c):
    return x**2 - c 

if num < 0:
    print('This has no square root in real numbers.')
else: 
    while True:
        guess = (low + high) / 2.0
        
        if quad_func(guess, num) == 0 or (abs(quad_func(guess, num)) < epsilon):
            print('numGuesses =', num_guesses)
            print(guess, 'is close to square root of', num)
            break
        
        print('low =', low, 'high =', high, 'ands =', guess)
        
        if quad_func(guess, num) * quad_func(low, num)> 0:
            low = guess
        else:
            high = guess
        
        num_guesses += 1