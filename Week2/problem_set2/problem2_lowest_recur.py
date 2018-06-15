# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def lowest_payment(balance, annual_interest_rate, notes):
    '''
    inputs  
    returns lowest payment
    '''
    def updated_balance(balance):
        for i in range(12):
            balance = (balance - 10 * notes) * (1 + annual_interest_rate / 12.0)
        return balance
    
    if updated_balance(balance) <= 0:
        return 'Lowest Payment: ' + str(10 * notes)
    else:
        return lowest_payment(balance, annual_interest_rate, notes + 1)

balance = 3329
annualInterestRate = 0.2

print(lowest_payment(balance, annualInterestRate, 0))