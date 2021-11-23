# 11047 동전 0
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coin = []
count = 0
for i in range(n):
    coin.append(int(input()))
for i in range(n):
    money = coin[n-1-i]
    time = k // money
    if k >= money:
        while k >= money:
            k = k - money*time
            count += time
print(count)
