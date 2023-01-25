# 1759 암호 만들기
from sys import stdin
input = stdin.readline

l, c = map(int, input().split())
letters = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
ans = []
result = []
letters.sort()

def is_recursion(i, ans):
    for letter in ans:
        if ord(letter) >= ord(i):
            return False
    return True

def is_print(ans):
    is_vowel = False
    not_vowel = 0
    for letter in ans:
        if letter in vowels:
            is_vowel = True
        else:
            not_vowel += 1
    if is_vowel and not_vowel > 1:
        return True
    else:
        return False

def dfs(n):
    if n == l:
        if is_print(ans):
            print(''.join(ans))
    else:
        for i in range(len(letters)):
            if n == 0:
                ans.append(letters[i])
                dfs(n + 1)
                ans.pop()
            else:
                if is_recursion(letters[i], ans):
                    ans.append(letters[i])
                    dfs(n+1)
                    ans.pop()

dfs(0)

