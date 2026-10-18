
# Problem 19: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input().strip()
    counts = Counter(s)

    for char, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]:
        print(char, count)
