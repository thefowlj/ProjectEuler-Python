#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

_max = 1000

palindromeArray = []

def isPalindromeNumber(n):
    numString = str(n)
    numStringLen = len(numString)
    q, r = divmod(numStringLen, 2)
    if(r == 0):
        print numString
        s1 = numString[0:q]
        print s1
        s2 = numString[q:len(numString)+1]
        print s2
        s2 = s2[::-1]
        if(s1 == s2):
            return True
    else:
        s1 = str(numString[0:q+1])
        s2 = str(numString[q-1:-1])
        s2 = str(s2[::-1])
        if(s1 == s2):
            return True
    return False

for i in range(1,_max):
    for j in range(1,_max):
        product = i*j
        if(isPalindromeNumber(product)):
            palindromeArray.append(product)

print max(palindromeArray)
