# 1307 문자사각형1

from sys import stdin
input = stdin.readline

n = int(input())
sqr = [['a']*n for _ in range(n)]
k= 65

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        sqr[j][i] = chr(k)
        k += 1
        if k > 90:
            k -= 26

for i in range(n):
    print(' '.join(sqr[i]))