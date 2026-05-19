#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:57:50 2026

@author: christyjm
"""

x = [100, 50, 400, 500]
x[1] = 200
x.append(600)
x.insert(2, 300)
x.remove(600)
x.pop(1)
x = x + [20, 60, 150, 10, 400]
x.sort()

print (x)

print(x.index(500))

if 500 in x:
    x[x.index(500)] = 490

print (x)