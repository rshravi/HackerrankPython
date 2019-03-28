#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    Min = scores[0]
    Max = scores[0]
    min_count, max_count = 0, 0
    for i in scores[1:]:
        if i < Min:
            Min = i
            min_count += 1
        if i > Max:
            Max = i
            max_count += 1
    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
