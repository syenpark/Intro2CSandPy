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
    previous_balance = balance
    monthly_interest_rate= annual_interest_rate / 12.0
    minimum_monthly_payment_rate = monthly_pyament_rate
    
    for i in range(12):
        minimum_monthly_payment = minimum_monthly_payment_rate * previous_balance
        monthly_unpaid_balance = previous_balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        previous_balance = updated_balance_each_month
    
    return 'Remaning balance: ' + str(round(updated_balance_each_month, 2))

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


print(remaning_balance(balance, annualInterestRate, monthlyPaymentRate))