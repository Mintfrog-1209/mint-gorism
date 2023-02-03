# 15654 N과 M (5) (23/02/03)

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = ['0']*M

def backtracking(k):
    if k == M:
        print(' '.join(temp))
    else:
        for i in range(N):
            if is_promising(str(arr[i])):
                temp[k] = str(arr[i])
                backtracking(k+1)
                temp[k] = '0'

def is_promising(x):
    if x in temp:
        return False
    else:
        return True
backtracking(0)
