# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def lowest_payment(balance, annual_interest_rate, monthly_payment):
    '''
    inputs  
    returns lowest payment
    '''
    previous_balance = balance
    monthly_interest_rate = annual_interest_rate / 12.0
    
    for i in range(12):
        minimum_fixed_monthly_payment = 10 * monthly_payment
        monthly_unpaid_balance = previous_balance - minimum_fixed_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        previous_balance = updated_balance_each_month
    
    if previous_balance <= 0:
        return 'Lowest Payment: ' + str(minimum_fixed_monthly_payment)
    else:
        return lowest_payment(balance, annual_interest_rate, monthly_payment + 1)

balance = 3329
annualInterestRate = 0.2


print(lowest_payment(balance, annualInterestRate, 0))