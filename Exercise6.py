#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:34:47 2026

@author: christyjm
"""


n = 5
result = 1
for i in range (n):
    result = result * (i + 1)
print ("Factorial of", n, "is", result)

import math
p = math.factorial(n)
print ("Factorial of", n, "is", p)