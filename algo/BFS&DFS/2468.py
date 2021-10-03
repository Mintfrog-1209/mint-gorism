from sys import stdin
from collections import deque
import copy
input = stdin.readline


def bfs(r, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] <= r:
                continue
            if graph[nx][ny] > r:
                graph[nx][ny] = 0
                queue.append((nx, ny))


original_graph = []
answer = []
n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    original_graph.append(list(map(int, input().split())))
for i in range(100):
    count = 0
    graph = copy.deepcopy(original_graph)
    for j in range(n):
        for h in range(n):
            if graph[j][h] > i:
                bfs(i, j, h)
                count += 1
    answer.append(count)
answer.sort(reverse=True)
print(answer[0])
