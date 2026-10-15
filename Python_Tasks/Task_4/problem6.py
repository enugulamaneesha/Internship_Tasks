# Problem 6: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = map(int, input().split())
unique_scores=sorted(set(arr),reverse=True)
print(unique_scores[1])
