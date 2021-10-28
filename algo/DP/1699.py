# 1699 제곱수의 합
from sys import stdin
input = stdin.readline

n = int(input())
num = [0]*100001

for i in range(1, n+1):
    num[i] = i

for i in range(1, n+1):
    j = 1
    while j*j <= i:
        num[i] = min(num[i], num[i-j*j]+1)
        j += 1

print(num[n])
