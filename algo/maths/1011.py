# 1011 Fly me to the Alpha Centauri
from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    range = 1
    count = 0
    while x < y:
        x += range
        y -= range
        range += 1
        count += 2
        if range - 1 <= y - x <= range:
            count += 1
            break
        elif y - x < range - 1:
            break
        elif range + 1 <= y - x <= 2 * range:
            count += 2
            break
    print(count)
