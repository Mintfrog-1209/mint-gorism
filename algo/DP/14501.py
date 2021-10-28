# 14501 퇴사
from sys import stdin
input = stdin.readline

n = int(input())
day = [0]*(n+1)
cost = [0]*(n+1)
result = [0]*(n+1)
temp = 0

for i in range(1, n+1):
    day[i], cost[i] = map(int, input().split())

for i in range(1, n+1):
    temp = 0
    if day[i] == 1:
        temp = result[i-1] + cost[i]
    for j in range(1, i):
        if day[j] + j == i+1:
            result[i] = max(result[j-1] + cost[j], result[i])
        result[i] = max(result[i], result[i-1])
    result[i] = max(temp, result[i])

print(result[n])
