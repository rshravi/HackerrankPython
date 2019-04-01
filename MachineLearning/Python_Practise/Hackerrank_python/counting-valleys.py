#https://www.hackerrank.com/challenges/counting-valleys/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c=0
    v=[]
    for i in range(0,n):
        if s[i]=='U':
            c+=1
            v.append(c)
        else:
            c-=1
            v.append(c)
    vc=0
    for i in range(0,len(v)):
        if v[i]==0 and v[i-1]==-1:
            vc+=1
    return vc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
