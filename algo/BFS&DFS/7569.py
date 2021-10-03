from sys import stdin
from collections import deque
input = stdin.readline
# graph[z][y][x]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        visit[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            if visit[nz][nx][ny] == 0 and graph[nz][nx][ny] == 0:
                queue.append((nx, ny, nz))
                graph[nz][nx][ny] = graph[z][x][y] + 1
                visit[nz][nx][ny] = 1


day = 0
m, n, h = map(int, input().split())
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
graph = [[] for i in range(h)]
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))
queue = deque()
isTrue = False
st = False
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((x, y, z))
bfs()
max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, graph[z][x][y])
if isTrue:
    print(-1)
else:
    print(max_num - 1)
