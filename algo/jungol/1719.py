# 1719 별삼각형2

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
if n % 2 == 0 or n > 100 or m > 4 or m <= 0:
    print("INPUT ERROR!")
elif m == 1:
    sqr = [[' ']*(n//2 + 1) for _ in range(n)]
    up = True
    idx = 0
    for i in range(n):   
        for j in range(n//2 + 1):
            if j <= idx:
                sqr[i][j] = '*'
        if idx == n//2:
            up = False
            idx -= 1                
        elif up:
            idx += 1
        else:
            idx -= 1
    for i in range(n):
        print(''.join(sqr[i]))
elif m == 2:
    sqr = [[' ']*(n//2 + 1) for _ in range(n)]
    down = True
    idx = n//2
    for i in range(n):   
        for j in range(n//2 + 1):
            if j >= idx:
                sqr[i][j] = '*'
        if idx == 0:
            down = False
            idx += 1                
        elif down:
            idx -= 1
        else:
            idx += 1
    for i in range(n):
        print(''.join(sqr[i]))
elif m == 3:
    sqr = [[' ']*n for _ in range(n)]
    idx = 0
    up = True
    for i in range(n):
        for j in range(n):
            if 0+idx <= j < n-idx:
                sqr[i][j] = '*'
        if idx == n//2:
            up = False
            idx -= 1                
        elif up:
            idx += 1
        else:
            idx -= 1
    for i in range(n):
        print(''.join(sqr[i]))
elif m == 4:
    sqr = [[' ']*n for _ in range(n)]
    idx = 0
    up = True
    for i in range(n):
        for j in range(n):
            if up:
                if 0+idx <= j <= n//2:
                    sqr[i][j] = '*'
            else:
                if n//2 <= j < n-idx:
                    sqr[i][j] = '*'
        if idx == n//2:
            up = False
            idx -= 1                
        elif up:
            idx += 1
        else:
            idx -= 1
    for i in range(n):
        print(''.join(sqr[i]))   

