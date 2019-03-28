#!/bin/python3
#https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys

# Complete the birthday function below.

def birthday(s, d, m):
    count=0
    for i in range(0,len(s)):
        if sum(s[i:i+m])==d:
            count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
