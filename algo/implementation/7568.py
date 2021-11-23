# 7568 덩치
from sys import stdin
input = stdin.readline

n = int(input())

stat = []
rank = [1]*n
for i in range(n):
    stat.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if stat[i][0] < stat[j][0] and stat[i][1] < stat[j][1]:
            rank[i] += 1

for i in range(n):
    print(rank[i], end=' ')
