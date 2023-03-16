# 4949 균형잡힌 세상
from sys import stdin
input = stdin.readline

while True:
    stack = []
    letters = input().rstrip('\n')
    is_balance = True
    if letters == '.':
        break
    for letter in letters:
        if letter == '(':
            stack.append(letter)
        elif letter == '[':
            stack.append(letter)
        elif letter == ')':
            if stack == []:
                is_balance = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                is_balance = False
                break
        elif letter == ']':
            if stack == []:
                is_balance = False
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                is_balance = False
                break
        elif letter == '.':
            if stack != []:
                is_balance = False
                break
            else:
                break
    if is_balance:
        print('yes')
    else:
        print('no')
