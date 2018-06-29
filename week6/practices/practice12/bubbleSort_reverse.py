# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def bubble_sort(L):
    """
    inputs : A list
    outputs: The list in a reverse order
    """
    swap = False
    
    while not swap:
        swap = True
        
        for i in range(1, len(L)):
            if L[i-1] < L[i]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]
    
test = [1, 5, 3, 8, 4, 2, 9, 6]
bubble_sort(test)

