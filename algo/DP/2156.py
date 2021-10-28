# 2156 포도주 시식
from sys import stdin
input = stdin.readline

n = int(input())
wine = [0]*(n+1)
dp = [0]*(n+1)
for i in range(1, n+1):
    wine[i] = int(input())
for i in range(1, n+1):
    if i == 1:
        dp[i] = wine[i]
    elif i == 2:
        dp[i] = dp[i-1] + wine[i]
    else:
        dp[i] = max(dp[i-3] + wine[i]+wine[i-1], dp[i-2]+wine[i])
        dp[i] = max(dp[i-1], dp[i])
print(dp[n])
