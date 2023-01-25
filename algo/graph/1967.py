from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
tree = {i:[] for i in range(n+1)}
for i in range(n-1):
  a, b, weight=map(int, input().split())
  tree[a].append((b,weight))
  tree[b].append((a,weight))

def bfs(s):
  q = deque()
  q.append((s,0))
  visited = [False]*n
  visited[s-1] = True

  result = [0,0]
  while q:
    now, cnt = q .popleft()
    for i in tree[now]:
      next_number , value = i[0] , i[1]
      if visited[next_number-1] == False:
        visited[next_number-1] = True
        q.append((next_number,cnt+value))
        if result[1] < cnt + value:
          result[0] = next_number
          result[1] = cnt+value

  return result

a = bfs(1)
b = bfs(a[0])
print(b[1])