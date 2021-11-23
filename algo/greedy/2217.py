# 2217 로프
from sys import stdin
input = stdin.readline

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
ans = 0
for i in range(n):
    ans = max(ans, rope[i]*(i+1))
print(ans)
