# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def multiply_five(x):
    return 5 * x

applyToEach(testList, multiply_five)

print(testList)
