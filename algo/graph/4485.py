# 4485 젤다
from sys import stdin
import heapq
input = stdin.readline
INF = 0xffffffff
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 1

while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]

    def dijkstra():
        heap = []
        heapq.heappush(heap, (graph[0][0], 0, 0))
        dist[0][0] = 0
        while heap:
            cost, y, x = heapq.heappop(heap)
            if x == y == n-1:
                print(f'Problem {count}: {dist[y][x]}')
                break
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    new_cost = cost + graph[ny][nx]
                    if new_cost < dist[ny][nx]:
                        dist[ny][nx] = new_cost
                        heapq.heappush(heap, (new_cost, ny, nx))

    dijkstra()
    count += 1



