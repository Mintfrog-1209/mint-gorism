# 1347 미로 만들기
from sys import stdin
input = stdin.readline

n = int(input())
commands = list(input().rstrip())
visited = [(0, 0)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
now_y = 0
now_x = 0
idx = 0
for command in commands:
    if command == 'L':
        if idx == 3:
            idx = 0
        else:
            idx += 1
    elif command == 'R':
        if idx == 0:
            idx = 3
        else:
            idx -= 1
    else:
        now_y += dy[idx]
        now_x += dx[idx]
        if (now_y, now_x) not in visited:
            visited.append((now_y, now_x))

print(visited)