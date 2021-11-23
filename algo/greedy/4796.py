# 4796 캠핑
from sys import stdin
input = stdin.readline
count = 1
while True:

    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    else:

        left = v % p
        if left >= l:
            num = (v//p)*l + l
        else:
            num = (v//p)*l + left

        print("Case ", count, ": ", num, sep="")
        count += 1
