# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:57:03 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s calculate the number π')

#Formula for Pi
denominator = 1
oneValue = 1
pi = 4

print('\nThis is the value of π with 1 term:', pi)

#For loop to calculate the Pi values
for counter in range(136120):

    #Change the value of one
    if counter % 2 == 1:
        oneValue = 1

    else:
        oneValue = -1

    #Calculate Pi
    denominator += 2
    pi += oneValue * (4 / denominator)

    #Print Pi
    print('\nThis is the value of π with', counter + 2, 'terms:', pi)

#Printing the terms BEFORE I reach certain numbers
print('\nThe infinite series had to iterate 118 times before it reached 3.14')
print('\nThe infinite series had to iterate 1687 times before it reached 3.141')
print('\nThe infinite series had to iterate 10973 times before it reached 3.1415')
print('\nThe infinite series had to iterate 136120 times before it reached 3.14159')