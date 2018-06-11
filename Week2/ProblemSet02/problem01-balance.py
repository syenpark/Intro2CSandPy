#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 00:41:48 2018

@author: syenpark
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0


for i in range(12):
    minimumMonthlyPayment =  balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    balance = updatedBalanceEachMonth
 
print("Remaining balance: ", round(balance, 2))
