# 1149 RGB거리
from sys import stdin
input = stdin.readline

n = int(input())
cost = [[0]*3]
dp = [[0]*3]

for i in range(n):
    cost.append(list(map(int, input().split())))
for i in range(1, n+1):
    temp = [0]*3
    temp[0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    temp[1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    temp[2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    dp.append(temp)
print(min(dp[n]))
