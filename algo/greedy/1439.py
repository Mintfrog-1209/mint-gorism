# 1439 뒤집기
from sys import stdin
input = stdin.readline

s = input().rstrip()
num0 = 0
num1 = 0
if s[0] == '0':
    num0 += 1
    for i in range(1, len(s)):
        if s[i] != s[i-1] and s[i] == '1':
            num1 += 1
        elif s[i] != s[i-1] and s[i] == '0':
            num0 += 1
elif s[0] == '1':
    num1 += 1
    for i in range(1, len(s)):
        if s[i] != s[i-1] and s[i] == '1':
            num1 += 1
        elif s[i] != s[i-1] and s[i] == '0':
            num0 += 1
print(min(num1, num0))
