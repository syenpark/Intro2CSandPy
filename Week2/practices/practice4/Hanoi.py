# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def Towers(n, source, target, auxiliary):
    if n == 1:
        print('move', source, 'to', target)
    else:    
        Towers(n-1, source, auxiliary, target)
        Towers(1, source, target, auxiliary)
        Towers(n-1, auxiliary, target, source)

Towers(3, 'P1', 'P3', 'P2')