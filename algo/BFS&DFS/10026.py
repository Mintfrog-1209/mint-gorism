# 10026 적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [input().rstrip() for _ in range(n)]
graph = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
visit = [[False]*n for _ in range(n)]
visit2 = [[False]*n for _ in range(n)]
for i in range(n):
    for letter in arr[i]:
        if letter == 'R':
            graph[i].append(0)
            graph2[i].append(0)
        elif letter == 'G':
            graph[i].append(1)
            graph2[i].append(0)
        else:
            graph[i].append(2)
            graph2[i].append(1)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
cnt2 = 0
def dfs(y, x, graph, visit):
    visit[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == graph[y][x] and visit[ny][nx] == False:
                dfs(ny, nx, graph, visit)    

for y in range(n):
    for x in range(n):
        if not visit[y][x]:
            dfs(y, x, graph, visit)
            cnt += 1

for y in range(n):
    for x in range(n):
        if not visit2[y][x]:
            dfs(y, x, graph2, visit2)
            cnt2 += 1

print(cnt, cnt2)