# 10162 전자레인지
from sys import stdin
input = stdin.readline

t = int(input())
a = b = c = 0
while t >= 10:
    if t >= 300:
        t -= 300
        a += 1
    elif t >= 60:
        t -= 60
        b += 1
    else:
        t -= 10
        c += 1
if t != 0:
    print(-1)
else:
    print(a, b, c)