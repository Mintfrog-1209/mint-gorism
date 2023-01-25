# 1012 유기농 배추
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    
    def dfs(x, y):
        arr[y][x] = 2
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx] == 1:
                    dfs(nx, ny)
    
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)
    