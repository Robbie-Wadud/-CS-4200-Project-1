# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:47:25 2020

@author: Robbie
"""

#Introduce the program
print('Let\'s create patterns with the asterisk!')

#Spacer
print('')

#Nested for loops to print out the first asterisk pattern
for counter in range(10):

    for anotherCounter in range(counter + 1):

        print('*', end='')

    print('')

#Spacer
print('')

#Nested for loops to print out the second asterisk pattern
for counter in range(10, 0, -1):

    for anotherCounter in range(counter):

        print('*', end='')

    print('')

#Spacer
print('')

#Var for the spaces
spaces = 0

#Nested for loops to print out the third asterisk pattern
for counter in range(10, 0, -1):

    for anotherCounter in range(spaces):

        print(end=' ')

    spaces += 1

    for anotherCounter in range(counter):
        print('*', end='')
    print('')

print('')


#Var for the spaces
spaces = 9

#Nested for loops to print out the fourth asterisk pattern
for counter in range(10):

    for anotherCounter in range(spaces):

        #Print the spaces
        print(end=' ')

    spaces -= 1

    for anotherCounter in range(counter + 1):
        print('*', end='')
    print('')