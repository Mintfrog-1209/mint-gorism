# 10773 제로
from sys import stdin
input = stdin.readline

n = int(input())
money = []
for i in range(n):
    m = int(input())
    if m != 0:
        money.append(m)
    else:
        money.pop()
print(sum(money))
