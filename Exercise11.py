#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:59:52 2026

@author: christyjm
"""

x = [4, 5, 8, 6, 4, 1, 2]
print ("Total number of items are", len(x))

for i in range(len(x)):
    if (i%2 == 0):
        print (x[i])


n = len(x)
if n == 0:
    print ("Empty list")
else:
    print("Number of items", n)
if ( n >= 4):
    print ("4th Element is", x[3])