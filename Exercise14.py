#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:35:17 2026

@author: christyjm
"""

x = [2, 3, 'apple', 6*2]

print(x)
print('Length x:', len(x))
print('apple' in x)
print('Second item:', x[1])

for item in x:
    print(item)
    
print('Three middle items', x[1:4])

x[0] = 1
print(x)

x.append(5)
print(x)

x.insert(1, 'abc')
print(x)

print (x.count('apple'))

#x.pop(2)
#print(x)

#x.remove('apple')
#print(x)

#del x[1]
#print(x)

#del x
#print(x)

#x.clear()
#print(x)

#y = [1, 'test']
#z = x + y
#print(z)

y = (1, 'test')
x.extend(y)
print(x)
print(y)