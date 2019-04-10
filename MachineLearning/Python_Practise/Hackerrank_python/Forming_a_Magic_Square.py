#https://www.hackerrank.com/challenges/magic-square-forming/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D%5B%5D=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    M = [[[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
         [[8, 3, 4], [1, 5, 9], [6, 7, 2]], [[2, 7, 6], [9, 5, 1],
                                             [4, 3, 8]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
         [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]]]

    sum = []
    for i in range(len(M)):
        c = 0
        for j in range(len(s)):
            for k in range(len(s)):
                if M[i][j][k] != s[j][k]:
                    c += abs(M[i][j][k] - s[j][k])
        sum.append(c)

    return (min(sum))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
