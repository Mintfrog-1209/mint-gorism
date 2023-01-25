# 4344 평균은 넘겠지
from sys import stdin
input = stdin.readline

c = int(input())
for i in range(c):
    n, *scores = list(map(int,input().split()))
    avg = sum(scores) / len(scores)
    student = 0
    for score in scores:
        if score > avg:
            student += 1
    answer = '{:.3f}'.format(student / len(scores) * 100)
    print(f'{answer}%')
