#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Project Euler Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?

numbers = {"1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five",
           "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten",
           "11" : "eleven", "12" : "twelve", "13" : "thirteen", "14" : "fourteen",
           "15" : "fifteen", "16" : "sixteen", "17" : "seventeen",
           "18" : "eighteen", "19" : "nineteen", "20" : "twenty",
           "30" : "thirty", "40" : "forty", "50" : "fifty", "60" : "sixty",
           "70" : "seventy", "80" : "eighty", "90" : "ninety"}

def RoundDown(num, divisor):
    return num - (num % divisor)


def NumToWords(n, numStr = ""):
    s = ""
    if n < 20 :
        s = numbers[str(n)]
    elif n >= 20 and n < 100 :
        if n % 10 == 0 :
            s = numbers[str(n)]
        else:
            x = RoundDown(n, 10)
            s = numbers[str(x)] + '-'
            s = NumToWords(n-x, s)
    elif n >= 100  and n < 1000 :
        s = numbers[str(n)[0]] + ' hundred'
        if n % 100 != 0 :
            s = NumToWords(n-RoundDown(n,100), s + " and ")
    elif n == 1000 :
        s = 'one thousand'

    return numStr + s

counter = 0

for i in range(1,1001):
    counter += len(NumToWords(i).replace(' ', '').replace('-', ''))

print counter
