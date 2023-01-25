# 1541 잃어버린 괄호
from sys import stdin
input = stdin.readline

num = list(map(str, input().split('-'))) # ['55', '50+40']
num2 = []
for i in range(len(num)):
    num2.append(list(map(int, num[i].split('+')))) # [55, [50,40]]
ans = sum(num2[0])
for i in range(1, len(num2)):
    ans = ans - sum(num2[i])
print(ans)
