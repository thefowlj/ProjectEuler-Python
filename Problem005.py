#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Project Euler Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

#This code could be optimized still, but it will output the correct answer.

x=40

def isEvenAndDivisible(n):
    i = 2

    while(i<=20):
        if n % i != 0:
            return False
        i += 1

    # Is divisible by 1-20, so return true!
    return True

while(not isEvenAndDivisible(x)):
    x += 2

print x
