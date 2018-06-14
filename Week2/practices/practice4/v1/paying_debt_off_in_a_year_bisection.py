#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:55:39 2018

@author: syenpark
"""
 
balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0

monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    
def remaning_balance(b, point):
    for i in range(12):
        minimumMonthlyPayment =  point
        monthlyUnpaidBalance = b - minimumMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        b = updatedBalanceEachMonth
    return b

while True:
    mid = (monthlyPaymentLowerBound  + monthlyPaymentUpperBound) / 2
    after_year = remaning_balance(balance, mid)
    
    if after_year == 0 or ( after_year < 0 and abs(after_year) < 0.1 ):
        print('Lowest Payment: ', round(mid, 2))
        break
    else:
        if remaning_balance(balance, monthlyPaymentLowerBound) * after_year > 0:
            monthlyPaymentLowerBound = mid
            
        else:
            monthlyPaymentUpperBound = mid
        