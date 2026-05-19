#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:32:09 2026

@author: christyjm
"""

import numpy as np

A = np.array([[3,  1,  1],
              [1, -1,  0],
              [0,  1, -1]])

B = np.array([2, 1, 0])

A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)

print('Solutions:', X)