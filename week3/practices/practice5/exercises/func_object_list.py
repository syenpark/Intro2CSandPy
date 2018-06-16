# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

def applyEachTo(L, x):
    result = []
    
    for f in L:
        result.append(f(x))
        
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))