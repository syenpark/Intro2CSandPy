# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def lowest_payment(balance, annual_interest_rate):
    '''
    inputs  
    returns lowest payment
    '''
    epsilon = 0.01
    lower = balance / 12.0
    upper = (balance * (1 + annual_interest_rate / 12.0)**12) / 12.0
    
    def updated_balance(balance, m):
        for i in range(12):
            balance = (1 + annual_interest_rate / 12.0) * (balance - m)
        
        return balance
    
    while True:
        mid = (lower + upper) / 2.0
        
        if updated_balance(balance, mid) == 0 or (upper - lower) / 2.0 < epsilon:
            return 'Lowest Payment: ' + str(round(mid, 2)) + " "
        elif updated_balance(balance, mid) * updated_balance(balance, lower) > 0:
            lower = mid
        else:
            upper = mid


balance = 320000
annualInterestRate = 0.2

print(lowest_payment(balance, annualInterestRate))