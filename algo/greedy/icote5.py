from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
balls = list(map(int, input().split()))
weight = [0]*11
answer = n*(n-1)//2
for k in balls:
    weight[k] += 1
for k in weight:
    answer -= k*(k-1)//2

print(answer)
