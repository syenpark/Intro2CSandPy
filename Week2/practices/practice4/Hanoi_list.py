# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
A = [3, 2, 1]
B = []
C = []
    
def Towers(n, source, target, auxiliary):
    
    if n > 0:
        Towers(n-1, source, auxiliary, target)
        target.append(source.pop())
        progress(A, B, C)
        Towers(n-1, auxiliary, target, source)

def progress(a, b, c):
    print('A', a)
    print('B',b)
    print('C',c)
    print('------------------')

Towers(3, A, C, B)