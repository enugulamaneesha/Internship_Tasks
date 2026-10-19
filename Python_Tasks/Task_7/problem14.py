# Problem 14: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    from collections import Counter
    n = len(s)

    if n % 2 != 0:
        return -1

    first = s[:n // 2]
    second = s[n // 2:]

    count1 = Counter(first)
    count2 = Counter(second)

    changes = 0
    for char in count1:
        changes += max(0, count1[char] - count2[char])

    return changes
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
