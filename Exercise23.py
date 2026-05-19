#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:03:11 2026

@author: christyjm
"""

def print_greeting(title, name):
    print("Hello, ", title.title(),". ", name.title(), sep="")
print_greeting("mr", "nguyen")


def print_grading(title, name, grade):
    print("Hello, ",title.title(),". ",name.title(), ", your grade is ", grade, sep="")
    print("You failed") if grade < 60 else print("You passed")
print_grading("mr","nguyen", 60)


def compute_sum(num1, num2, num3):
    return num1 + num2 + num3

total = compute_sum(1, 1.5, 2.4)
print("Total is", total)


def compute_stat(a, b):
    s = a + b
    d = a -b
    p = a * b 
    return s, d, p
    
sum_val, diff_val, product_val= compute_stat(3, 2)
print("Sum is", sum_val)
print("Difference is", diff_val)
print("Product is", product_val)


def odd_or_even(num):
    print("Even")if num%2 == 0 else print ("Odd")

odd_or_even(2)


def get_month_name(num):
    month_name = ["January", "February", "March"]
    return month_name[num-1]

get_month_name(2)