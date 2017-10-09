#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Project Euler Problem 6
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

x = 0
y = 0
i = 0

while(i <= 100):
    x += i
    y += i**2
    i += 1

print str((x**2) - y)
