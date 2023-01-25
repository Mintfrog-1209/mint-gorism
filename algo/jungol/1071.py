# 1071 약수와 배수

from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

x = 0
y = 0
for num in nums:
    if m % num == 0:
        x += num

for num in nums:
    if num % m == 0:
        y += num

print(x)
print(y)