# 1966 프린터 큐
from sys import stdin
from collections import deque
import heapq
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    rare = []
    paper = deque()
    p = list(map(int, input().split()))

    for i in range(n):
        heapq.heappush(rare, p[i] * -1)
        paper.append((p[i], i))
    count = 0
    while paper:
        x, y = paper.popleft()
        if x == rare[0] * -1:
            heapq.heappop(rare)
            count += 1
            if y == m:
                break
        else:
            paper.append((x, y))

    print(count)
