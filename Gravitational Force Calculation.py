#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:25:30 2026

@author: christyjm
"""

import math

G = 6.674 * math.pow(10, -11)
r = 384400000
m_earth = 5.972 * math.pow(10, 24)
m_moon = 7.348 * math.pow(10,22)

F = G * ((m_earth * m_moon)/math.pow(r, 2))

print("The gravitional force between the Earth and the Moon is, ", F)