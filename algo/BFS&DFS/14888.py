# 14888 연산자 끼워넣기
from sys import stdin
from itertools import permutations
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sign_num = list(map(int, input().split()))
sign = []
for i in range(sign_num[0]):
    sign.append('+')
for i in range(sign_num[1]):
    sign.append('-')
for i in range(sign_num[2]):
    sign.append('*')
for i in range(sign_num[3]):
    sign.append('/')
arr1 = permutations(sign, n-1)
arr2 = set(arr1)
o_sign = list(arr2)
max_value = -1000000000
min_value = 1000000000
for ord in o_sign:
    ans = nums[0]
    for i in range(1,len(ord)+1):
        if ord[i-1] == '+':
            ans = ans + nums[i]
        if ord[i-1] == '-':
            ans = ans - nums[i]
        if ord[i-1] == '*':
            ans = ans * nums[i]
        if ord[i-1] == '/':
            if ans < 0:
                ans = (ans*-1 // nums[i])*-1
            else:
                ans = ans // nums[i]
    if ans >= max_value:
        max_value = ans
    if ans <= min_value:
        min_value = ans
print(max_value)
print(min_value)