#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:05:16 2018

@author: syenpark
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0

def cal_balance(bal, mon):

    minimumMonthlyPayment =  bal * monthlyPaymentRate
    monthlyUnpaidBalance = bal - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    bal = updatedBalanceEachMonth
    
    if mon == 1:
        return bal
    else:
        mon -= 1
    
    
    return cal_balance(bal, mon)
 
print("Remaining balance: ", round(cal_balance(balance, 12), 2))