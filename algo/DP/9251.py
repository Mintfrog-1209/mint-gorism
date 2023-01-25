# 9251 LCS
# TopDown(재귀)
from sys import stdin
input = stdin.readline

a = input().rstrip()
b = input().rstrip()
ans = 0
memo =[[0]*len(b) for _ in range(len(a))]

def lcs(idx_1, idx_2):
    if idx_1 == len(a) or idx_2 == len(b):
        return 0
    else:
        for i in range(idx_1, len(a)):
            for j in range(idx_2, len(b)):
                if a[i] == b[j]:
                    memo[idx_1][idx_2] = max(lcs(i+1, j+1) + 1, memo[idx_1][idx_2])
    return memo[idx_1][idx_2]
                
ans = lcs(0,0)
print(ans)