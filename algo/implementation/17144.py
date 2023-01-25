# 17144 미세먼지 안녕!
from sys import stdin
input = stdin.readline

y, x, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(y)]
room2 = room.deepcopy()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dust(room):
    for j in range(y):
        for i in range(x):
            if room[j][i] > 0:
                k = room[j][i]
                for h in range(4):
                    ny = j + dy[h]
                    nx = i + dx[h]
                    if 0 <= ny < y and 0 <= nx < x:
                        room[ny][nx] -= k//5
                        room[j][i] += k//5
    return room
def purify(room):
    for j in range(y):
        if room[j][0] == -1:
            for i in range(x-1):
                if i == 0:
                    room2[j][1] = 0
                else:
                    room2[j][i+1] = room[j][i]
                


