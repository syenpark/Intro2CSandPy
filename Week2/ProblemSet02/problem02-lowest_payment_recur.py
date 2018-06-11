#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:22:29 2018

@author: syenpark
"""

balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0

def foo(b, a, ii):
    
    for i in range(12):
        minimumMonthlyPayment =  ii*10
        monthlyUnpaidBalance = b - minimumMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        b = updatedBalanceEachMonth
    
    if b > 0:
        ii += 1
        return foo(balance, annualInterestRate, ii)
    else:
        return ii
    
    
print(foo(balance, annualInterestRate, 1)*10)