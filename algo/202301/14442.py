# 14442 벽 부수고 이동하기 2 (2023/01/28)

from sys import stdin
from collections import deque
import copy
input = stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(K+1)]
for _ in range(N):
    t1 = list(map(int, input().rstrip()))
    for i in range(K+1):
        t2 = copy.deepcopy(t1)
        graph[i].append(t2)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = -999999999

def bfs():
    ans = [-1] * (K+1)
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
                    if wall > 0 and graph[wall-1][ny][nx] == graph[wall][y][x] + 1:
                        continue
                    graph[wall][ny][nx] = graph[wall][y][x] - 1
                    queue.append((wall, ny, nx))
                if graph[wall][ny][nx] == 1:
                    if wall < K:
                        graph[wall+1][ny][nx] = graph[wall][y][x] - 1
                        queue.append((wall + 1, ny, nx))
    for i in range(K+1):
        if graph[i][N-1][M-1] == 0:
            continue
        else:
            ans[i] = graph[i][N-1][M-1] * -1 + 1
    ans.sort()
    for a in ans:
        if a == -1:
            continue
        else:
            return a
    if N == M == 1:
        return 1
    else:
        return -1

print(bfs())
