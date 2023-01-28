# 2206 벽 부수고 이동하기 (2023/01/28)

from sys import stdin
from collections import deque
import copy
input = stdin.readline

N, M = map(int, input().split())
graph = [[],[]]
for _ in range(N):
    t1 = list(map(int, input().rstrip()))
    t2 = copy.deepcopy(t1)
    graph[0].append(t1)
    graph[1].append(t2)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = -999999999

def bfs():
    queue = deque([])
    queue.append((0,0,0))
    while queue:
        wall, y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[wall][ny][nx] == 0:
                    if ny == 0 and nx == 0:
                        continue
                    graph[wall][ny][nx] = graph[wall][y][x] - 1
                    queue.append((wall, ny, nx))
                if graph[wall][ny][nx] == 1:
                    if wall == 0:
                        graph[wall+1][ny][nx] = graph[wall][y][x] - 1
                        queue.append((wall + 1, ny, nx))
    if graph[0][N-1][M-1] == 0:
        graph[0][N-1][M-1] = INF
    if graph[1][N-1][M-1] == 0:
        graph[1][N-1][M-1] = INF
    if graph[0][N-1][M-1] == INF and graph[1][N-1][M-1] == INF:
        if N == M == 1:
            return 1
        else:
            return -1
    return min(graph[0][N-1][M-1] * -1 + 1, graph[1][N-1][M-1] * -1 + 1)

print(bfs())
