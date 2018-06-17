# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
            
    return aTup[::2]
            
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))