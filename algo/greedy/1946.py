# 1946 신입사원
from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    array = []
    count = 1
    for i in range(n):
        array.append(map(int, input().split()))
    score1 = dict(array)
    k = score1[1]
    for i in range(2, n+1):
        if score1[i] < k:
            count += 1
            k = score1[i]
    print(count)
