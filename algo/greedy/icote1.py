from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
answer = 1
for num in arr:
    if num <= answer :
        cnt += 1
    if cnt == answer:
        cnt = 0
        answer += 1
        
print(answer-1)
