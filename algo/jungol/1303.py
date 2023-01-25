# 1303 숫자사각형 1
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
cnt = 1
for _ in range(n):
    for _ in range(m):
        print(cnt, end=" ")
        cnt += 1
    print()