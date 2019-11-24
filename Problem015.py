#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Project Euler Problem 15
# Lattice Paths
# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down, there are exactly 6 routes
# to the bottom right corner.
#
# In mathematics, a simple NE Lattice Path can be calculated using
# a binomial coefficient to count the number of different paths to reach
# another coordinate. Going from the origin (0,0) to (n,k) can be calculated
# using binomial coefficient
# Binomial(n+k,n)
# = (n+k)!/((k!)(n+k-k)!)
# = (n+k)!/((k!)(n!))
#
# In this case, we can start from the origin (0,0) to
# (20,20)

import math

n = 20
k = 20

paths = math.factorial(n+k)/(math.factorial(k)*math.factorial(n))

print paths
