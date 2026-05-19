#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:04:00 2026

@author: christyjm
"""

x = (2, 3, 'apple', 6*2)

print(x)

#x[0] = 1
x.append(5)

print(x)

print('Length x:', len(x))

print('apple' in x)

print('Second item:', x[1])

for item in x:
    print(item)
    
print('Three middle items', x[1:4])