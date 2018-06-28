# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def get_ratios(L1, L2):
    """
    inputs : L1 and L2 are two lists of equal length of numbers
    returns: A list containing L1[i]/L2[i]
    """
    ratios = []
     
    for i in range(min(len(L1), len(L2))):
        try:
            t = float(L1[i]) / float(L2[i])
            ratios.append(t)
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad arg')            
    
    return ratios


