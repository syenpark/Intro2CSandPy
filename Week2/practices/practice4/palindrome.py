# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def isPalindrome(s):
    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

def extract_characters(s):
    character = []
    characters = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    
    for c in s:
        if c in alphabets:
            character.append(c)
            
    characters = characters.join(character)
    return characters
    
    
print("")
print('Is eve a palindrome?')
print(isPalindrome(extract_characters('eve')))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome(extract_characters('Able was I, ere I saw Elba')))