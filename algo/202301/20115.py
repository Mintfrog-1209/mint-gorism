# 20115 에너지 드링크 (2023/01/20)
from sys import stdin
input = stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
for i in range(n-1):
    drinks[n-1] += drinks[i] / 2
if drinks[n-1] % 1 == 0:
    print(int(drinks[n-1]))
else:
    print(drinks[n-1])