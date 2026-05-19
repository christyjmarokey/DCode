#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:17:57 2026

@author: christyjm
"""

import numpy as np
x = np.array([[1, 2],
[3, 4]])

y = np.array([[3, 1],
[4, 2]])

x1 = x + 1
#print(x1)

x2 = x*y
#print(x2)

x3 = x/y
#print(x3)
      
x4 = np.dot(x,y)
print(x4)