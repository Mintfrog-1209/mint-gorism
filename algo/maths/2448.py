# 2448 별 찍기 11
from sys import stdin
input = stdin.readline

n = int(input())
k = 2*n - 1
pic = [[' ']* k for _ in range(n)]

def triangle(k, y, x):
    n = k // 2
    if k == 3:
        pic[y][x] = '*' # pic[0][2]
        pic[y+1][x-1] = '*'
        pic[y+1][x+1] = '*' # pic[1][1], pic[1][3]
        pic[y+2][x-2] = '*' # pic[2][0] pic[2][1]
        pic[y+2][x-1] = '*'
        pic[y+2][x] = '*'
        pic[y+2][x+1] = '*'
        pic[y+2][x+2] = '*'
    else:
        triangle(n, y + n, x - n) # triangle(3, 3, 2) triangle(3, 3, 8) triangle(3, 0, 5)
        triangle(n, y + n, x + n) # (6, 6, 5) (6, 6, 17) (6, 0, 11)
        triangle(n, y, x) # (3, 9, 2) (3, 9, 8) (3, 6, 5)
triangle(n, 0, k//2)
for p in pic:
    print(''.join(p))
