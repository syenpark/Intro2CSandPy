# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def biggest(dic):
    big_animal = ['', 0]
    
    if not dic:
        return None
    
    for key in dic:
        if big_animal[1] < len(dic[key]):
            big_animal = [key, len(dic[key])]
        
    return big_animal[0]

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))