# 2046 숫자사각형4

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

if m == 1:
    cnt = 1
    for _ in range(n):
        for i in range(1, n+1):
            print(cnt, end= " ")
        print()
        cnt += 1
elif m == 2:
    cnt = 1
    for _ in range(n):
        if cnt%2:
            for i in range(1, n+1):
                print(i, end=" ")
        else:
            for i in range(n, 0, -1):
                print(i, end=" ")
        print()
        cnt += 1
else:
    cnt = 1
    for _ in range(n):
        for i in range(1, n+1):
            print(i*cnt, end=" ")
        print()
        cnt += 1
