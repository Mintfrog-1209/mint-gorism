from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int, input().split()))
a = [0]*n
for i in range(n):
    for j in range(i+1):
        a[i] += num[j]

print(a)
