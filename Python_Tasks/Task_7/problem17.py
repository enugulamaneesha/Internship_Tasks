# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys



def separateNumbers(s):
    # Write your code here
    length = len(s)

    for i in range(1, length // 2 + 1):
        first = s[:i]

        if first.startswith('0'):
            continue

        current = int(first)
        built = ''

        while len(built) < length:
            built += str(current)
            current += 1

        if built == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
