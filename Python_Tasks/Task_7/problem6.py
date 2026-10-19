# Problem 6: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem
#!/bin/python3

import math
import os
import random
import re
import sys



def pangrams(s):
    # Write your code here
    letters = set(s.lower())
    return "pangram" if len(letters.intersection(set("abcdefghijklmnopqrstuvwxyz"))) == 26 else "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
