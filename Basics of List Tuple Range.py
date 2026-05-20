#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:13:27 2026

@author: christyjm
"""

x = ['a', 'bc','e']
print(x,"has type", type(x)) #list

y = [1,2,5.,'a',"bc"]
y[0] = 5
print(y, "has type", type(y)) #list

z = (2,3, 'apple', 6*2)
print(z, "has type", type(z)) #tuple

print(type(range (4))) #range


a = ["apple", "banana", "cherry"]
print (a, "has type", type(a))
print (a, "has", len(a), "items")

b = list(range(4))
print (b, "has type", type (b))
print (b, "has", len(b), "items")

c = ["abc", 12, True, "def", 5.2,]
for item in c:
    print(item, "has type", type(item))
    
print("First item is ", c[0])
print("Last item is", c[len(c) - 1])

for i in range (len(c)):
    print("The", i+1, "th item is ", c[i])

print("Last item is", c[-1])
print("Second last item is", c[-2])   

this_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(this_list[3:5])
print(this_list[3:])
print(this_list[:5])
print(this_list[-3:-1])