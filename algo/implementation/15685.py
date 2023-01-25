from sys import stdin
input = stdin.readline

n = int(input())
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
arr = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1
    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)
    for i in move:
        ny = y + dy[i]
        nx = x + dx[i]
        arr[ny][nx] = 1
        y, x = ny, nx
for j in range(100):
    for i in range(100):
        if arr[j][i] and arr[j + 1][i] and arr[j][i + 1] and arr[j + 1][i + 1]:
            ans += 1

print(ans)