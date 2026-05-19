#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:58:05 2026

@author: christyjm
"""

n = 9876
z = 0

while n > 0:
    z = z + n % 10
    n = n // 10

print ("Sum is", z)


n = 123
last_digit = n%10
print("Last Digit", last_digit)
n = n // 10
print ("New Number ", n)
last_digit = n%10
print("Last Digit", last_digit)
n = n // 10
print ("New Number ", n)
n = n // 10
print ("New Number ", n)


n = 12345
total = 0
count = 0
while (n > 0):
    last_digit = n%10
    print ("Digit is", last_digit)
    count = count + 1
    total = total + last_digit
    n = n//10

print ("Sum is", total)
print ("Count is", count)