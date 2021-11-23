# 1789 수들의 합
from sys import stdin
input = stdin.readline

s = int(input())
n = 1
finish = False
while finish == False:
    if s < n*(n+1)//2:
        print(n-1)
        finish = True
    else:
        n += 1
