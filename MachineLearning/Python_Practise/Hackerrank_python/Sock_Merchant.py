#https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d={}
    pairs=0
    for i in ar:
        d[i]=d.get(i,0)+1

    for k,v in d.items():
        if d[k]%2==0:
            pairs+=d[k]/2
        else:
            pairs+=d[k]//2

    return int(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
