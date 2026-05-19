#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:12:50 2026

@author: christyjm
"""

thisList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(thisList[2:5]) 
print(thisList[:4]) 
print(thisList[3:]) 
print(thisList[-3:-1])


thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")
    print("Number of apples in the list: ", thisList.count('apple'))


x = [1, 2, 2, 'a', 2, 1, 'a', 2]
print("Number of 2 in the list:", x.count(2))
print("Number of a in the list:", x.count('a'))

x = [1, 2, 5., 'a', "bc"]
x[1:3] = [3, 4]
print(x)

x = [1, 2, 5., 'a', "bc"]
x[0] = 5
print(x)

x = [1, 2, 5., 'a', "bc"]
x[1:3] = [3, 4, 6]
print(x)

x = [1, 2, 5., 'a', "bc"]
x[:3] = [3]
print(x)

thisList = ["apple", "banana", "cherry"] 
thisList.append("orange")
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList.insert(1, ["orange", "kiwi"])
print(thisList)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

thisList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisTuple = ("mango", "pineapple")
thisList.extend(thisTuple)
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)

thisList = [100, 50, 65, 82, 23]
thisList.sort()
print(thisList)
