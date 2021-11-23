# 1715 카드 정렬하기 (우선순위 큐)
from sys import stdin
import heapq
input = stdin.readline
n = int(input())
card = []
sum = 0
for i in range(n):
    card.append(int(input()))
heapq.heapify(card)

while len(card) != 1:
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)
    temp = num1 + num2
    sum += temp
    heapq.heappush(card, temp)
print(sum)
