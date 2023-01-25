# 1291 구구단
from sys import stdin
input = stdin.readline

while True:
    s, e = map(int, input().split())
    if 1 < s < 10 and 1 < e < 10:
        if s > e:
            for i in range(1, 10):
                for j in range(s, e-1, -1):
                    if j*i < 10:
                        print(j, "*", i, "= ", j*i, end="   ")
                    else:
                        print(j, "*", i, "=", j*i, end="   ")
                print()
        elif s < e:
            for i in range(1, 10):
                for j in range(s, e+1):
                    if j*i < 10:
                        print(j, "*", i, "= ", j*i, end="   ")
                    else:
                        print(j, "*", i, "=", j*i, end="   ")
                print()
        else:
            for i in range(1, 10):
                if s*i < 10:
                    print(s, "*", i, "= ", s*i, end="   ")
                else:
                    print(s, "*", i, "=", s*i, end="   ")
                print()
        break
    else:
        print("INPUT ERROR!")