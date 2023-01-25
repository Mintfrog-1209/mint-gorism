# 2813 소수의 개수

from sys import stdin
input = stdin.readline

m, n = map(int, input().split())

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

cnt = 0

for i in range(m, n+1):
    if is_prime(i):
        cnt += 1
print(cnt)