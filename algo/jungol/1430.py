# 1430 숫자의 개수

from sys import stdin
input = stdin.readline

a = int(input())
b = int(input())
c = int(input())
x = a * b * c
num = [0]*10

while x:
    y = x % 10
    num[y] += 1
    x = x // 10

for i in range(10):
    print(num[i])
