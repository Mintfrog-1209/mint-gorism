# 10844 쉬운 계단수
from sys import stdin
input = stdin.readline

stair = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
n = int(input())

for i in range(n-1):
    nstair = [0]*10
    for j in range(10):
        if j == 0:
            nstair[j] = stair[i][1]
        elif j == 9:
            nstair[j] = stair[i][8]
        else:
            nstair[j] = stair[i][j-1] + stair[i][j+1]
    stair.append(nstair)
print(sum(stair[n-1]) % 1000000000)
