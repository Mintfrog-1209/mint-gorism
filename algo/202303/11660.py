# 11660 구간 합 구하기 5
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = []
arr2 = []
dp = [[0]*(N+1) for _ in range(N+1)]
ans = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N+1):
    for j in range(N+1):
        if i != 0 and j != 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    ans.append(sum)

for i in range(M):
    print(ans[i])

