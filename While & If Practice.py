#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:26:58 2026

@author: christyjm
"""

x = input("Enter a number: ") 
number_x = int(x)
key = 6

while number_x != key:
    print ("Incorrect")
    
    if (number_x < key):
        print ("Too Small. Guess again")
    else:
        print ("Too Large. Guess again")

    x = input("Enter a number: ") 
    number_x = int(x)

else:
    print("You entered correct number")
    
    
