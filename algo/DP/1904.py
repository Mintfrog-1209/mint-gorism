# 1904 01타일
from sys import stdin
input = stdin.readline

n = int(input())
tile = [0]*(n+1)

for i in range(1, n+1):
    if i == 1:
        tile[i] = 1
    elif i == 2:
        tile[i] = 2
    else:
        tile[i] = tile[i-1] + tile[i-2]
        tile[i] %= 15746
print(tile[n])
