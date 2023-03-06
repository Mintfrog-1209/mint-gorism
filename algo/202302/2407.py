# 2407 조합 (23/02/16)
from sys import stdin
from fractions import Fraction
input = stdin.readline

n, m = map(int, input().split())
ans = 1
for i in range(1, m+1):
    ans = Fraction(ans * (n-i+1), i)
print(ans)
