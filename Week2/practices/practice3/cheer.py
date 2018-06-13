# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""

an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input('I will cheer for you! Enter a word: ')
times = int(input('Enthusiasm level (1-10): '))



for c in word:
    if c in an_letters:
        definite_article = 'an'
    else:
        definite_article = 'a '
        
    print('Give me', definite_article, c + '!', c)
    
print('What does that spell?')

for i in range(times):
    print(word, "!!!")    