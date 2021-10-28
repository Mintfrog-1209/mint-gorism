# 11052 카드 구매하기
from sys import stdin
input = stdin.readline

n = int(input())
card = list(map(int, input().split()))
dp = [0]*(n+1)
cost = []
for i in range(1, n+1):
    cost = []
    for j in range(i):
        cost.append(dp[i-j-1] + card[j])
    dp[i] = max(cost)
print(dp[n])
