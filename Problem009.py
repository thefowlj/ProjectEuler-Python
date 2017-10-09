#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Project Euler Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

maxSum = 1000
a = 0
c = 0

def isInt(n):
    return n % math.trunc(n) == 0

for i in range(maxSum):
    b = a + 1
    for j in range(maxSum):
        c = a**2 + b**2
        c = math.sqrt(c)
        # if(isInt(c)):
        #     print str(a) + ", " + str(b) + ", " + str(c)
        if(isInt(c) and (a + b + c) == 1000):
            print a*b*c
        b += 1
    a += 1

print "FAIL"
