# 2630  색종이 만들기
from sys import stdin

input = stdin.readline

n = int(input())
square = []
for i in range(n):
    square.append(list(map(int, input().split())))


def sum1(x, y, n):
    sum = 0
    for j in range(n):
        for i in range(n):
            sum += square[y+j][x+i]
    if sum == n*n or sum == 0:
        return True
    else:
        return False


def cut1(x, y, n):
    if n == 1:
        if square[y][x] == 0:
            return 1
        else:
            return 0
    else:
        if sum1(x, y, n):
            if square[y][x] == 0:
                return 1
            else:
                return 0
        else:
            m = n//2
            return cut1(x, y, m) + cut1(x + m, y, m) + cut1(x, y+m, m) + cut1(x+m, y+m, m)


def cut2(x, y, n):
    if n == 1:
        if square[y][x] == 0:
            return 0
        else:
            return 1
    else:
        if sum1(x, y, n):
            if square[y][x] == 0:
                return 0
            else:
                return 1
        else:
            m = n//2
            return cut2(x, y, m) + cut2(x + m, y, m) + cut2(x, y+m, m) + cut2(x+m, y+m, m)


print(cut1(0, 0, n))
print(cut2(0, 0, n))
