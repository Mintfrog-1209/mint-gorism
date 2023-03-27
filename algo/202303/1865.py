# 1865 웜홀 (23/03/17)
from sys import stdin
input = stdin.readline
INF = 0xffffffff
TC = int(input())

for _ in range(TC):
    answer = 'NO'
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S,E,-T))
    def bellman_ford():
        dist = [INF]*(N+1)
        dist[1] = 0
        for i in range(N):
            for S, E, T in edges:
                if dist[E] > dist[S] + T:
                    if i == N-1:
                        return False
                    dist[E] = dist[S] + T
        return True

    if not bellman_ford():
        answer = 'YES'
    print(answer)