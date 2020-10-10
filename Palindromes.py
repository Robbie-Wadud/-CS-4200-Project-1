# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 03:07:06 2020

@author: Robbie
"""

#Introduce the program
print('Let\'s play with palindromes!')

#In case the user types in a non-int
while True:
    try:
        number = int(input('Please type in a five-digit number: '))
        break
    except ValueError:
        print('\nYou have typed in something invalid.')

#Validation Loop
while number < 9999 or number > 99999:
    print('\nYou have NOT typed in a five-digit number.')
    
    #In case the user types in a non-int
    while True:
        try:
            number = int(input("Please type in a five-digit number: "))
            break
        
        except ValueError:
            print('\nYou have typed in something invalid.')

#Spacer
print('\n', end = '')

#Need this var to do calculations
floor = 1

#Need this list
digits = [None]

#For loop put the digits into a list
for digit in range(5):
    digit = ((number % (floor * 10)) // floor)
    
    floor *= 10
    
    #Add the digit to the list
    digits.append(digit)

#Getting rid of the first none value
digits.pop(0)

#Put the digits into a string
palindrome = [str(integer) for integer in digits]

#Combine the String list so it's one number
palindrome = ''.join(palindrome)

#Convert the palindrome into an int
palindrome = int(palindrome)

#If statement to decide if the number is a palindrome
if number == palindrome:
    print(number, 'was a palindrome!')

else:
    print(number, 'was not a palindrome.')