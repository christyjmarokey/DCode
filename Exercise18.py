#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:02:54 2026

@author: christyjm
"""

x = [1, 2, 3]
result=2*x
print(result)

x = [1, 2, 3]
result=[2 * num for num in x]
print(result)

import numpy as np
x = np.array([1, 2, 3])
result=2*x
print(result)

import time
import numpy as np
x = [i for i in range(10000000)]
start = time.time()
result = [2 * num for num in x]
print('Computation time with list:', (time.time()-start), 'ms')
x_np = np.array(x)
start = time.time()
result_np= 2*x_np
print('Computation time with numpy:', (time.time()-start), 'ms')