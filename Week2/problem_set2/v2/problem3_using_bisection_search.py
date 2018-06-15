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
    monthly_interest_rate = annual_interest_rate / 12.0
    
    monthly_payment_lower_bound = balance / 12.0
    monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    
    def update(low, high):
        previous_balance = balance
        for i in range(12):
            minimum_fixed_monthly_payment = (low + high) / 2.0
            monthly_unpaid_balance = previous_balance - minimum_fixed_monthly_payment
            updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
            previous_balance = updated_balance_each_month
        return updated_balance_each_month
    
    while True:
        if update(monthly_payment_upper_bound, monthly_payment_lower_bound) == 0 or (monthly_payment_upper_bound - monthly_payment_lower_bound) / 2.0 < 0.01:
            return (monthly_payment_upper_bound + monthly_payment_lower_bound) / 2.0
        elif update(monthly_payment_upper_bound, monthly_payment_lower_bound) * update(monthly_payment_lower_bound, monthly_payment_lower_bound) > 0:
            monthly_payment_lower_bound = (monthly_payment_upper_bound + monthly_payment_lower_bound) / 2.0
        else:
            monthly_payment_upper_bound = (monthly_payment_upper_bound + monthly_payment_lower_bound) / 2.0

balance = 320000
annualInterestRate = 0.2


print(lowest_payment(balance, annualInterestRate, 0))