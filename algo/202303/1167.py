# 1167 트리의 지름 (23/03/28)
from sys import stdin
from collections import deque
input = stdin.readline
INF = 0xffffffff

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    line = list(map(int, input().split()))
    k = line[0]
    for j in range(1, len(line)-2, 2):
        E, L = line[j], line[j+1]
        graph[k].append((E, L))
def bfs(start):
    visit = [False]*(V+1)
    visit[start] = True
    queue = deque([])
    queue.append((start, 0))
    answer = [start, 0]
    while queue:
        dest, dist = queue.popleft()
        for next_dest, next_dist in graph[dest]:
            if not visit[next_dest]:
                visit[next_dest] = True
                new_dist = dist + next_dist
                if new_dist > answer[1]:
                    answer = [next_dest, new_dist]
                queue.append((next_dest, new_dist))
    return answer

answer1 = bfs(1)
answer2 = bfs(answer1[0])
print(answer2[1])
