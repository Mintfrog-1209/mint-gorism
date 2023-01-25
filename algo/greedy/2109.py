# 2109 순회강연
from sys import stdin
import heapq
input = stdin.readline

n = int(input())
schedule = []
for _ in range(n):
    p, d = map(int, input().split())
    schedule.append([p, d])
schedule = sorted(schedule, key=lambda x: x[1])
result = []
for s in schedule:
    heapq.heappush(result, s[0])
    if len(result) > s[1]:
        heapq.heappop(result)
print(sum(result))
