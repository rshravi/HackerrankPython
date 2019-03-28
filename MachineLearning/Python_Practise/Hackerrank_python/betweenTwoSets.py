#!/bin/python3

import os
import sys
import functools
#
# Complete the getTotalX function below.
#

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b
def lcm(a, b):
    return a * b // gcd(a, b)
def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first

def getTotalX(a, b):
    #min_gcd = functools.reduce(gcd, b)
    min_gcd =my_reduce(gcd, b)
    #max_lcm = functools.reduce(lcm, a)
    max_lcm =my_reduce(lcm, a)
    print("GCD: ", min_gcd)
    print("LCM: ", max_lcm)
    count = sum([1 for x in range(max_lcm, min_gcd + 1, max_lcm) if min_gcd % x == 0])

    return count




if __name__ == '__main__':


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)
    print("Total:" ,total)


