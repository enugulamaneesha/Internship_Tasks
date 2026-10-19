# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys



def isValid(s):
    # Write your code here
    from collections import Counter
    frequencies = Counter(Counter(s).values())

    if len(frequencies) == 1:
        return "YES"

    if len(frequencies) == 2:
        (f1, c1), (f2, c2) = sorted(frequencies.items())

        if (f1 == 1 and c1 == 1) or (f2 == f1 + 1 and c2 == 1):
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
