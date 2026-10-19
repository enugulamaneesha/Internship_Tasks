
# Problem 12: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem


#!/bin/python3

import math
import os
import random
import re
import sys



def makingAnagrams(s1, s2):
    # Write your code here
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)

    deletions = 0
    for char in set(count1) | set(count2):
        deletions += abs(count1[char] - count2[char])

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
