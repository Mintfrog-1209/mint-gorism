# 1541 잃어버린 괄호
from sys import stdin
input = stdin.readline

num = list(map(str, input().split('-')))
num2 = []
for i in range(len(num)):
    num2.append(list(map(int, num[i].split('+'))))
ans = sum(num2[0])
for i in range(1, len(num2)):
    ans = ans - sum(num2[i])
print(ans)
