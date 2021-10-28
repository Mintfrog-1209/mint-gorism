# 1932 정수 삼각형
from sys import stdin
input = stdin.readline

n = int(input())
tri = [[0]]
dp = [[0]]
for i in range(n):
    tri.append(list(map(int, input().split())))
dp.append(tri[1])
for i in range(2, n+1):
    temp = []
    for j in range(i):
        if j == 0:
            temp.append(dp[i-1][0] + tri[i][0])
        elif j == i-1:
            temp.append(dp[i-1][j-1] + tri[i][j])
        else:

            temp.append((max(dp[i-1][j-1], dp[i-1][j])) + tri[i][j])
    dp.append(temp)
print(max(dp[n]))
