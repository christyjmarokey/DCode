#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:30:51 2026

@author: christyjm
"""

x = [1, 2, 2, 3, 4, 5, 6]
for n in x:
    if n % 2 == 0:
        x.remove(n)
print(x)

x = [1, 2, 2, 3, 4, 5, 6]
y = [num for num in x if num % 2 == 1]
print(y)
print("Total number of items: ", len (x))
print("Number of odd items: ", len(y))
print("Number of even items: ", (len(x) - len(y)))


x = [1,3,2,6,5,4]
y = []
for num in x:
    if num % 2 == 0:
        x.remove(num)
print(x)

x =[1,3,2,6,5,4]
y = [num for num in x if num %2 == 0]
z = [num for num in x if num %2 != 0]
print(y)
print(z)
    

