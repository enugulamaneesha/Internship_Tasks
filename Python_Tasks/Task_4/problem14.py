
# Problem 14: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    country_stamps = set()

    for _ in range(n):
        country_stamps.add(input().strip())

    print(len(country_stamps))
