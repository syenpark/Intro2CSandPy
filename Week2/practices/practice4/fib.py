# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
    
num = int(input('Enter a whole number: '))

def fib(x):
    if x < 2:
        return 1
    return fib(x-1) + fib(x-2)

print(fib(num))