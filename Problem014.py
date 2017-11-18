#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Project Euler Problem 11
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

sequenceList = []
longestChainLen = 0
longestStartNum = 0
longestList = []

def sequenceFun(n):
    if(n > 1):
        if(n % 2 == 0):
            return n/2
        else:
            return 3*n + 1
    elif(n == 1):
        return 1
    else:
        return -1

def sequenceArray(startingNum):
    sArray = []
    if(startingNum > 13):
        n = startingNum
        sArray.append(n)
        while(n > 1):
            n = sequenceFun(n)
            sArray.append(n)
        return sArray
    return -1

for i in range(14,10**6):
    tempArray = sequenceArray(i)
    l = len(tempArray)
    if(l > longestChainLen):
        longestStartNum = i
        longestChainLen = l
    print i

print longestStartNum
