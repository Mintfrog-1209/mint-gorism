# 2775 부녀회장이 될테야
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(15):
        apt[0][i] = i
    for i in range(1, 15):
        for j in range(1, 15):
            apt[i][j] = apt[i][j-1] + apt[i-1][j]
    print(apt[k][n])