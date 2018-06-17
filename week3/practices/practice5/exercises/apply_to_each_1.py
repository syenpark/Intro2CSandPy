# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def multiply_five(x):
    return x*5

testList = [1, -4, 8, -9]

applyToEach(testList, multiply_five)