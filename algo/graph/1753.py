# 1753 최단경로
from sys import stdin
import heapq
input = stdin.readline

V, E = map(int, input().split())
k = int(input())
INF = 0xffffff
dist = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V+1)]

def dijkstra(start):
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        now_w, now = heapq.heappop(heap)
        if dist[now] < now_w:
            continue
        for w, next in graph[now]:
            next_w = w + now_w
            if next_w < dist[next]:
                dist[next] = next_w
                heapq.heappush(heap, (next_w, next))

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((w, v))

dijkstra(k)

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
