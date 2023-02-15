# 9251 LCS (23/02/15)

from sys import stdin
input = stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for i in range(len(B)+1):
    for j in range(len(A)+1):
        if i == 0 or j == 0:
            continue
        elif A[j-1] == B[i-1]:
            dp[i][j] = max(1 + dp[i-1][j-1], dp[i-1][j], dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(B)][len(A)])