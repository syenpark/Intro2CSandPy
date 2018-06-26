# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""

def selection_sort(L):
    for count in range(0, len(L)):
        for i in range(count, len(L)):
            if L[i] < L[count]:
                L[i], L[count] = L[count], L[i]
        
L = [5, 1, 4, 2]
selection_sort(L)
