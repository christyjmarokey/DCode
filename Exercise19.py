#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:09:14 2026

@author: christyjm
"""

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print('Number of dimensions:', arr.ndim)
print('Dimension:',arr.shape)
print('Data type',arr.dtype)

import numpy as np
arr = np.array([[[1., 2, 3], [4, 5, 6]],
[[7, 8, 9], [0, 1, 2]]])
print(arr)
print('Number of dimensions:', arr.ndim)
print('Dimension:',arr.shape)
print('Data type',arr.dtype)


