# 15649 M과N (1)
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
visited = [0]*n
answer = []
def mn():
    if len(answer) == m :
        print(*answer)
       
        
    else:
        for i in range(n):
            if i+1 not in answer:
                answer.append(i+1)
                mn()
                answer.pop()
mn()