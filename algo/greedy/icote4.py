from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 1
for n in arr:
    if answer < n:
        break
    answer += n
print(answer)