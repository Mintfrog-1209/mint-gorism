# 14698 전생슬라
from sys import stdin
import heapq
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    cost = 1
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost *= (a*b)
        heapq.heappush(heap, a*b)
    print(cost%1000000007)
