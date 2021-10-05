from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
sum = 0
for i in range(n):
    c.append((i, b[i]))
a.sort()
c.sort(key=lambda x: x[1], reverse=True)
k = [0]*n
for i in range(n):
    k[c[i][0]] = a[i]
for i in range(n):
    sum += k[i] * b[i]
print(sum)
