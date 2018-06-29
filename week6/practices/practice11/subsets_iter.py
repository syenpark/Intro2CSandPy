# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def gen_subsets(L):
    """
    A set that consists of n elements has 2^n possible subsets.
    Then, all possible subsets can be represented by binary number.
    If an element is 1, this means containing this position's value.
    Else, this position's value does not belong to a subset.
    
    For instance,
    (a, b) has 2^2 possible subsets;
     0 0   ()     emty subset
     0 1   (b)
     1 0   (a)
     1 1   (a, b)
    
    
    inputs:  A list
    returns: All possible subsets of the list
    """
    temp = []
    subsets = []
    
    # if L is empty, return [[]]
    if not L:
        return [subsets]
    
    # A set that consists of n elements has 2^n possible subsets
    for i in range(1 << len(L)):
       as_binary = return_binary(i, len(L))
       
       for i2 in range(len(L)):
           if as_binary[i2]:
               temp.append(L[i2])
       
       subsets.append(temp)
       temp = []
        
    return subsets

def return_binary(n, length):
    """
    inputs : n is a decimal number to be represented as a binary number
             length is the length of a target list
    returns: n to be a binary number in a list
    """
    temp = []
    
    while n:
        temp.insert(0, n%2)
        n //= 2
            
    while len(temp) != length:
        temp.insert(0, 0)
        
    return temp
    
            
test = [1,2,3,4]
print(gen_subsets(test))