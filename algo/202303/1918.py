# 1918 후위 표기식
from sys import stdin
from collections import deque

formular = list(input())
ans = ''
stack = []
for char in formular:
    if char == '(':
        stack.append(char)
    elif char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(char)
    elif char == '+' or char == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        ans += char


while stack:
    ans += stack.pop()
print(ans)