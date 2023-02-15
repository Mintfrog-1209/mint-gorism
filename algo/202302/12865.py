# 12865 평범한 배낭 (23/02/03)

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
weight = []
value = []
for _ in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if i == 0 or j == 0:
            pass
        elif weight[i-1] <= j:
            dp[i][j] = max(value[i-1] + dp[i-1][j - weight[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])




