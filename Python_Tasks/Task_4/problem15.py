# Problem 15: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem
s=int(input())
d={}
for i in range(s):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(len(d))
for i in d.values():
    print(i,end=" ")
