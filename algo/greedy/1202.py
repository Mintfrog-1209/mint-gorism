# 1202 보석 도둑
from sys import stdin
import heapq
input = stdin.readline

heap = []
bag = []
aheap = []
money = 0
n, k = map(int, input().split())
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(heap, (m, v))
for i in range(k):
    bag.append(int(input()))
bag.sort()
for i in range(k):
    while heap and bag[i] >= heap[0][0]:
        (m, v) = heapq.heappop(heap)
        heapq.heappush(aheap, -v)
    if aheap:
        value = heapq.heappop(aheap) * -1
        money += value
    elif not heap:
        break

print(money)
