# 12865 평범한 배낭 (23/02/03)

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
bag = []
for _ in range(N):
    W, V = map(int, input().split())
    bag.append((W, V))
dp = [0]*(K+1)
packed = [False]*N
bag.sort()

def pack(x):
    for i in range(N):
        if x + bag[i][0] < N:
            return

def is_promising(x):
    if not packed[x]:
        return