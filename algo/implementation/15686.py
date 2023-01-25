# 15686 치킨 배달
from sys import stdin
from itertools import combinations
input = stdin.readline

n, m = map(int, input().split())
house = []
chicken = []
for i in range(n):
    house.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if house[i][j] == 2:
            chicken.append([i, j])
            house[i][j] = 0

result = list(combinations(chicken, m))
min_distance = 999999
for i in range(len(result)):
    distance = 0
    for a in range(n):
        for b in range(n):
            if house[a][b] == 1:
                temp = 999999
                for j in range(m):
                    temp = min(
                        temp, abs(a - result[i][j][0]) + abs(b - result[i][j][1]))
                distance += temp
    min_distance = min(min_distance, distance)

print(min_distance)
