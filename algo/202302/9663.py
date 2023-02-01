# 9663 N-Queen (23/02/01)

from sys import stdin
input = stdin.readline

n = int(input())
ans = 0
arr = [0]*n

def nqueen(k):
    global ans
    if k == n:
        ans += 1
    else:
        for i in range(n):
            arr[k] = i
            if is_promising(k):
                nqueen(k+1)
        

def is_promising(k):
    for i in range(k):
        if arr[i] == arr[k] or k-i == abs(arr[k] - arr[i]):
            return False
    return True

nqueen(0)
print(ans)