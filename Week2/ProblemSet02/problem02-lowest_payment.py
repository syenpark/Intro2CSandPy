#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:22:29 2018

@author: syenpark
"""

ii = 1

while True:
    balance = 4773
    annualInterestRate = 0.2
    monthlyInterestRate = annualInterestRate / 12.0
    
    for i in range(12):
        minimumMonthlyPayment =  ii*10
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        balance = updatedBalanceEachMonth

    
    if balance > 0:
        ii += 1
    else:
        break
    
print(ii*10)