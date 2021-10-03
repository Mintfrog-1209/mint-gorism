from sys import stdin
input = stdin.readline
count = 0


def dfs(x, y, t):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = t
        dfs(x-1, y, t)
        dfs(x+1, y, t)
        dfs(x, y-1, t)
        dfs(x, y+1, t)
        return True
    return False


n = int(input())

graph = []
house = []
count = 0
for i in range(n):
    graph.append(list(map(int, input().rstrip("\n"))))

result = 2
for i in range(n):
    for j in range(n):
        if dfs(i, j, result) == True:
            result += 1
print(result-2)
if result != 2:
    for i in range(2, result):
        home = 0
        for j in range(n):
            home += graph[j].count(i)
        house.append(home)
house.sort()
for i in house:
    print(i)
