# 11725 트리의 부모 찾기 (23/03/22)
from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque([])

def tree():
    visited[1] = True
    queue.append(1)
    while queue:
        a = queue.popleft()
        for son in graph[a]:
            if not visited[son]:
                queue.append(son)
                visited[son] = True
            else:
                parent[a] = son

tree()
for i in range(2, N+1):
    print(parent[i])



