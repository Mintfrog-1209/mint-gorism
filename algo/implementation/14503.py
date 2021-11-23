# 14503 로봇 청소기
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
count = [1]
for i in range(n):
    room.append(list(map(int, input().split())))
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r, c, d, count):
    room[r][c] = 2
    if room[r + dr[d-1]][c + dc[d-1]] == 0:
        if d == 0:
            d = 3
        else:
            d += -1
        count[0] += 1

        clean(r + dr[d], c + dc[d], d, count)
    elif room[r + dr[d-2]][c + dc[d-2]] == 0:
        if d == 0:
            d = 2
        elif d == 1:
            d = 3
        else:
            d += -2
        count[0] += 1

        clean(r + dr[d], c + dc[d], d, count)
    elif room[r + dr[d-3]][c + dc[d-3]] == 0:
        if d == 3:
            d = 0
        else:
            d += 1
        count[0] += 1

        clean(r + dr[d], c + dc[d], d, count)
    elif room[r + dr[d]][c + dc[d]] == 0:
        count[0] += 1

        clean(r + dr[d], c + dc[d], d, count)
    else:
        if room[r + dr[d-2]][c + dc[d-2]] == 2:

            clean(r + dr[d-2], c + dc[d-2], d, count)


clean(r, c, d, count)
print(count[0])
