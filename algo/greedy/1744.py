# 1744 수 묶기
from sys import stdin
import heapq
input = stdin.readline

heap = []
heapminus = []
sum = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x >= 0:
        heapq.heappush(heap, (-x, x))
    else:
        heapq.heappush(heapminus, x)
while len(heap) > 1:
    a = heapq.heappop(heap)[1]
    b = heapq.heappop(heap)[1]
    if b > 1:
        sum += a*b
    elif b == 1:
        sum += a+b
    else:
        heapq.heappush(heap, (-b, b))
        sum += a

while len(heapminus) > 1:
    a = heapq.heappop(heapminus)
    b = heapq.heappop(heapminus)
    sum += a*b

if heap:
    a = heapq.heappop(heap)[1]
    if heapminus:
        b = heapq.heappop(heapminus)
        if a != 0:
            sum += a
            sum += b
    else:
        sum += a
if heapminus:
    a = heapq.heappop(heapminus)
    sum += a
print(sum)
