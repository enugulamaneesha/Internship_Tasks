# Problem 17: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other = set(map(int, input().split()))

    if not A.issuperset(other) or A == other:
        result = False
        break

print(result)
