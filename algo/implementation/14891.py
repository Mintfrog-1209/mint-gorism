from sys import stdin
from collections import deque
input = stdin.readline

gears = []
result = 0
def gear_left(start, dir):
    if start < 0 or gears[start][2] == gears[start+1][6]:
        return
    if gears[start][2] != gears[start+1][6]:
        gear_left(start-1, -dir)
        gears[start].rotate(dir)

def gear_right(start, dir):
    if start > 3 or gears[start-1][2] == gears[start][6]:
        return
    if gears[start-1][2] != gears[start][6]:
        gear_right(start+1, -dir)
        gears[start].rotate(dir)

for i in range(4):
    gears.append(deque(list(map(int, input().rstrip()))))
n = int(input())

for _ in range(n):
    num, dir = map(int,input().split())
    num -= 1
    gear_right(num+1, -dir)
    gear_left(num-1, -dir)
    gears[num].rotate(dir)

for i in range(4):
    result += 2**(i) * gears[i][0]
print(result)
