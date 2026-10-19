# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys



def gameOfThrones(s):
    # Write your code here
    from collections import Counter
    frequencies = Counter(s)
    odd_counts = sum(1 for count in frequencies.values() if count % 2 != 0)

    return "YES" if odd_counts <= 1 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
