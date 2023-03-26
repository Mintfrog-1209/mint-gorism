# 11404 플로이드 (2023/03/26)
from sys import stdin
input = stdin.readline
INF = 0xffffffffff

n = int(input())
m = int(input())
graph = [[INF]*(n) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for i in range(n):
    graph[i][i] = 0
for i in range(n):
    for j in range(n):
        for h in range(n):
            graph[j][h] = min(graph[j][h], graph[j][i] + graph[i][h])
for i in range(n):
    print(' '.join(str(k) if k != INF else '0' for k in graph[i]))