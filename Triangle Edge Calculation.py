#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:54:58 2026

@author: christyjm
"""
import math

AB = 7
AC = 9
AB_square = pow (7, 2)
AC_square = pow (9, 2)


angle_rad = math.radians(45)   # returns 0.785398...
cos45 = math.cos(angle_rad)

BC_square = AB_square + AC_square - 2 * AB * AC * cos45

BC = math.sqrt(BC_square)

print("The edge BC of the triangle is ", BC )