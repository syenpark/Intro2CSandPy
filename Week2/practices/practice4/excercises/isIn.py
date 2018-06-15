# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if not aStr:
        return False
    
    mid = len(aStr) // 2
    
    if char == aStr[mid]:
        return True
    else:
        if 2 > mid:
            return False
        
        if char > aStr[mid]:
            return isIn(char, aStr[mid:])
        else:
            return isIn(char, aStr[:mid+1])
        
print(isIn('c', 'adehq'))