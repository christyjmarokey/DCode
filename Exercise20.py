#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:13:02 2026

@author: christyjm
"""


import numpy as np
x = np.array([1, 2, 3])
x1 = x + 1
print(x1)

x2 = x*3
print(x2)

x3 = x/2
print(x3)

x4 = x ** 2
print(x4)


x = np.array([1, 2, 3])
y = np.array([4, 1, 2])

x1 = x - y
print(x1)

x2 = x*y
print(x)

x3 = x/y 
print(x3)


x4 = np.dot(x,y)
print(x4)