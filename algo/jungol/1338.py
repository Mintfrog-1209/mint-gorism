# 1338 문자삼각형1

from sys import stdin
input = stdin.readline

n = int(input())
k = 65
x = n -1
sqr = [[' ']*n for _ in range(n)]

while x <= (n-1)*2:
    for i in range(n):
        for j in range(n):
            if j + i == x:
                sqr[i][j] = chr(k)
                k += 1
                if k > 90:
                    k -= 26
    x += 1

for i in range(n):
    print(' '.join(sqr[i]))