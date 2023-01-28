# 1238 파티 (2023/01/28)

from sys import stdin
import heapq
input = stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = 0xffffffff
for _ in range(M):
    start, end, t = map(int, input().split())
    graph[start].append((t, end))

def dijkstra(graph, start):
    dist = [INF]*(N+1)
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
ans = 0
for i in range(1, N+1):
    temp = dijkstra(graph, i)[X] + dijkstra(graph, X)[i]
    if ans < temp:
        ans = temp
print(ans)
