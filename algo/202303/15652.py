# 15652 N과 M(4) (23/03/17)
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
temp = [0]*M

def backtracking(k):
    if k == M:
        print(' '.join(str(n) for n in temp))
    else:
        x = max(temp)
        for i in range(1, N+1):
            if i >= x:
                temp[k] = i
                backtracking(k+1)
                temp[k] = 0

backtracking(0)