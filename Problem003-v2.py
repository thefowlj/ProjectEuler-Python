#!/usr/bin/python
# -*- coding: utf-8 -*-
# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# function is_prime(n)
#     if n ≤ 1
#         return false
#     else if n ≤ 3
#         return true
#     else if n mod 2 = 0 or n mod 3 = 0
#         return false
#     let i ← 5
#     while i * i ≤ n
#         if n mod i = 0 or n mod (i + 2) = 0
#             return false
#         i ← i + 6
#     return true

import random

_numTrials = 10

def isSmallPrime(num):
    if(num <=1):
        return False
    elif(num <= 3):
        return True
    elif(num % 3 == 0):
        return False

    for index in range(5,num):
        if(num % index == 0 or num % (index + 2) == 0):
            return False
    return True

def isProbablePrime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_numTrials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite

def getFactors(num):
    # x = num
    # # simplePrimes = [2,3,5,7,11]
    # # for i in range(len(simplePrimes)):
    # #     q, r = divmod(num,simplePrimes[i])
    # #     if(r == 0):
    # #         return [simplePrimes[i],q]
    # #
    # # q, r = divmod(num,simplePrimes[len(simplePrimes)-1])
    # # if(r == 0):
    # #     return [simplePrimes[len(simplePrimes)-1],q]
    # # num = q
    # i = 0
    # while True:
    #     i += 1
    #     q, r = divmod(num,2)
    #     if r == 0 :
    #         return [i*2,q]
    #     num = q
    #     print num
    # return [1,x]


    secondFactor = 0
    firstFactor = 1

    while(firstFactor < num):
        firstFactor = firstFactor + 1
        if(num % firstFactor == 0):
            secondFactor = num / firstFactor
            print secondFactor
            return [firstFactor,secondFactor]

def arrayPrimeFactorization(factors):
    primeFactors = []
    for index in range(len(factors)):
        if(isProbablePrime(factors[index])):
            primeFactors.append(factors[index])
        else:
            arrayPrimeFactorization(getFactors(factors[index]))
    return primeFactors

def findPrimeFactors(n):
    primeFactors = []
    while True:
        factors = getFactors(n)
        primeFactors.append(factors[0])
        if isProbablePrime(factors[1]):
            primeFactors.append(factors[1])
            return primeFactors
        n = factors[1]

print findPrimeFactors(3247923847298347)
