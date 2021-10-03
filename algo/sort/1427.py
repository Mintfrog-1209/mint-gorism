from sys import stdin
input = stdin.readline

num = list(input().rstrip())
num.sort(reverse=True)
for n in num:
    print(n, end='')
