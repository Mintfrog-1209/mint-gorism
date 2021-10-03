from sys import stdin
input = stdin.readline

num = []
n = int(input())
for i in range(n):
    num.append(int(input()))
num.sort()
for n in num:
    print(n)
