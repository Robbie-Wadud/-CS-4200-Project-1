# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:23:59 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s find Pythagorean Triples!')

print('\nFormat- "This is one of the Pythagorean Triples:" side1, side2, hypotenuse')

#Nested for loop that will calculate Pythagorean Triples
for a in range(1,20):    
    for b in range(1,20):
        for c in range(1,20):
            
            #
            if (a ** 2) + (b ** 2) == c ** 2:
                print('\nThis is one of the Pythagorean Triples: {}, {}, {}'.format(a, b, c))