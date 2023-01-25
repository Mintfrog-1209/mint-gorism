# 1436 영화감독 숌
from sys import stdin
input = stdin.readline

n = int(input())
num = 0
cnt = 0
while True:
    if num == n:
        break
    cnt += 1
    if '666' in str(cnt):
        num += 1
print(cnt)
