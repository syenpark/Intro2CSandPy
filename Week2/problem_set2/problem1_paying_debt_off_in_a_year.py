# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def remaning_balance(balance, annual_interest_rate, monthly_pyament_rate):
    '''
    inputs  
    returns remaing balance
    '''
    for i in range(12):
        balance = balance * (1 - monthly_pyament_rate) * (1 + annual_interest_rate / 12.0)
    
    return 'Remaning balance: ' + str(round(balance, 2))

balance = 206
annualInterestRate = 0.2
monthlyPaymentRate = 0.06

print(remaning_balance(balance, annualInterestRate, monthlyPaymentRate))