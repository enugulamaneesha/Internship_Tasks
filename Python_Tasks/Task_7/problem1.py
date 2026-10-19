
# Problem 1: Set .symmetric_difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    print(len(english.symmetric_difference(french)))
