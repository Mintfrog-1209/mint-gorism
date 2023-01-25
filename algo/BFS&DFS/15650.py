# 15650 M과N (2)
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
visited = [0]*n
answer = []

def mn(k):
    if len(answer) == m :
        print(*answer)
       
        
    else:
        for i in range(n):
            if i+1 not in answer and i+1 > k: 
                answer.append(i+1)
                mn(i+1)
                answer.pop()
mn(0)