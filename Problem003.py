#!/usr/bin/python
# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def getFactors(num):
    simpleFactors = getSimpleFactors(num)
    if(simpleFactors != False):
        return simpleFactors

    firstFactor = 0
    secondFactor = 0
    firstFactor = num

    while(firstFactor > 0 ):
        firstFactor = firstFactor - 1
        print firstFactor
        if(num % firstFactor == 0):
            secondFactor = num / firstFactor
            return [firstFactor,secondFactor]

def getSimpleFactors(num):
    if(num % 2 == 0):
        return [2, num / 2]
    elif(num % 3 == 0):
        return [3, num / 3]
    elif(num % 5):
        return [5, num / 5]
    elif(num % 7):
        return [7, num / 7]
    elif(num % 11):
        return [11, num / 11]
    else:
        return False

def isPrimeFactor(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

def arrayPrimeFactorization(factors):
    primeFactors = []
    for index in range(len(factors)):
        if(isPrimeFactor(factors[index])):
            primeFactors.append(factors[index])
        else:
            arrayPrimeFactorization(getFactors(factors[index]))
    return primeFactors



print(arrayPrimeFactorization(getFactors(600851475143)))
