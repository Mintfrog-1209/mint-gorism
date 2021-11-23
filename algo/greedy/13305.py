# 13305 주유소
from sys import stdin
input = stdin.readline

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
oil = city[0]
dp = [oil*road[0]]
for i in range(1, n-1):
    oil = min(oil, city[i])
    dp.append(dp[i-1] + oil*road[i])
print(dp[n-2])
