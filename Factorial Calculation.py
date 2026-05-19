#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:18:37 2026

@author: christyjm
"""
import math

n = 10

if n >= 0:
    j = 1
    for i in range (1, n + 1):
        j = j * i

print ("by using my own code", j)
    
k = math.factorial(n)
print ("by using math function", k)