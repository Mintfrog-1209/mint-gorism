# 9465 스티커
from sys import stdin
input = stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    stick1 = list(map(int, input().split()))
    stick2 = list(map(int, input().split()))

    dp1 = [0]
    dp2 = [0]
    dp1.append(stick1[0])
    dp2.append(stick2[0])
    for i in range(2, n+1):
        dp1.append(max(dp2[i-1]+stick1[i-1], dp1[i-2] +
                   stick1[i-1], dp2[i-2]+stick1[i-1]))
        dp2.append(max(dp1[i-1]+stick2[i-1], dp2[i-2] +
                   stick2[i-1], dp1[i-2]+stick2[i-1]))
    print(max(dp1[n], dp2[n]))
