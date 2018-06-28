# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over \
    a significant distance.'
        
        
        