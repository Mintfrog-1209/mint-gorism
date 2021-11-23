# 16953 A -> B
from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
count = 1

while b > a:
    if b % 10 == 1:
        b = b // 10
        count += 1
    elif (b % 10) % 2 == 0:
        b = b // 2
        count += 1
    else:
        break

if b != a:
    print(-1)
else:
    print(count)
