# 14501 퇴사
from sys import stdin
input = stdin.readline

n = int(input())
day = [0]*n
cost = [0]*n
result = [0]*n

for i in range(n):
    day[i], cost[i] = map(int, input().split())

for i in range(n):
    j = i
    while j < n:
        pay = cost[j]
        j += day[j]
        if j <= n:
            result[i] += pay
print(max(result))
