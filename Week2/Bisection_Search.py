#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:15:04 2018

@author: syenpark
"""
low = 0
high = 100

print('Please think of a number between 0 and 100!')

while True:
    num = (low + high)//2
    
    response = input('Is your secret number '+ str(num) +'? \n\
    Enter \'h\' to indicate the guess is too high. \
    Enter \'l\' to indicate the guess is too low. \
    Enter \'c\' to indicate I guessed correctly.')

    if response == 'h':
        high = num

    elif response == 'l':
        low = num
        
    elif response == 'c':
        print('Game over. Your secret number was: ', num)
        break
    else:
        print('Sorry, I did not understand your input.')