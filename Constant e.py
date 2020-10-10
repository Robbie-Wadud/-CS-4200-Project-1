# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 03:07:07 2020

@author: Robbi
"""

#Import Statements
import math

#Introduce the program
print('Let\'s calculate the number e')

#Var to hold the total
e = 0

for denominator in range(10):
    e += (1 / (math.factorial(denominator)))

#Spacer
print('\n', end = '')

print('This is the estimation of e with 10 terms: ', e)