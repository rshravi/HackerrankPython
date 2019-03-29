#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def check_leapYear(year):
    check=False
    if (1700<=year<=1917) and (year%4==0):
        check=True
        return check
    elif (1918<=year<=2700):
        if (year%400==0) or ((year%4==0) and (year%100 !=0)):
            check=True
            return check
def dayOfProgrammer(year):
    leap_year="12.09."
    noleap_year="13.09."
    transyear="26.09."
    if year == 1918:
        return transyear+str(year)
    if check_leapYear(year):
        return leap_year+str(year)
    else:
        return noleap_year+str(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
