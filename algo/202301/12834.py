# 12834 주간 미팅 (2023/01/20)
from sys import stdin
import heapq
input = stdin.readline

INF = 0xffffff
N, V, E = map(int, input().split())
A, B = map(int, input().split())
homes = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]
ans = 0

for _ in range(E):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

def dijkstra(graph, start):
    dist = [INF] * (V+1)
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
                heapq.heappush(queue, [distance, new_dest])
    return dist

for home in homes:
    da = dijkstra(graph, home)[A]
    db = dijkstra(graph, home)[B]
    if da == INF:
        ans += -1
    else:
        ans += da
    if db == INF:
        ans += -1
    else:
        ans += db
print(ans)