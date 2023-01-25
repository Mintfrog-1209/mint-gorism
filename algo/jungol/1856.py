# 1856 숫자사각형2
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
cnt1 = 1
cnt2 = 1

for _ in range(n):
    for _ in range(m):
        if cnt2%2:
            print(cnt1, end=" ")
            cnt1 += 1
        else:
            print(cnt1, end=" ")
            cnt1 -= 1
    if cnt2%2:
        cnt1 += m-1
    else:
        cnt1 += m+1        
    cnt2 += 1
    print()