# 1916 최소비용 구하기 (2023/01/25)
from sys import stdin
import heapq
input = stdin.readline

n = int(input())
m = int(input())
INF = 0xffffffff
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
x, y = map(int, input().split())

def dijkstra(graph, start):
    dist = [INF]*(n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        current_dist, current_dest = heapq.heappop(queue)
        if dist[current_dest] < current_dist:
            continue
        for new_dist, new_dest in graph[current_dest]:
            distance = current_dist + new_dist
            if distance < dist[new_dest]:
                dist[new_dest] = distance
                heapq.heappush(queue, (distance, new_dest))
    return dist

print(dijkstra(graph, x)[y])

    