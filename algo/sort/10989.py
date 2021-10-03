from sys import stdin
input = stdin.readline
# 계수 정렬

n = int(input())

count = [0] * (10001)
for i in range(n):
    k = int(input())
    count[k] += 1
for i in range(1, 10001):
    for j in range(count[i]):
        print(i)
