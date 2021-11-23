# 1339 단어 수학
from sys import stdin
input = stdin.readline

n = int(input())
alpha = [0]*26
sum = 0
for i in range(n):
    word = input().rstrip()
    l = len(word)
    for j in range(l):
        k = ord(word[l-1-j]) - 65
        alpha[k] += 10**j

alpha.sort(reverse=True)
for i in range(10):
    sum += alpha[i] * (9-i)
print(sum)
