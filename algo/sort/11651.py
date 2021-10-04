from sys import stdin
input = stdin.readline

n = int(input())
coord = []
for i in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))
coord.sort(key=lambda x: x[0])
coord.sort(key=lambda x: x[1])
for x, y in coord:
    print(x, y)
