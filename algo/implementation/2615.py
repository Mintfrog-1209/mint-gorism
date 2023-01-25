# 2615 오목
from sys import stdin
input = stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
is_end = False
dy = [-1, 0, 1, 1, -1, -1, 0, 1] # 가장 왼쪽 혹은 가장 위의값 출력해야되므로 
dx = [1, 1, 1, 0, 0, -1, -1, -1]
def omok(i, j, k):
    if 0 <= i+dy[k] <= 18 and 0<= j+dx[k] <= 18: # IndexError 방지
        if board[i][j] == board[i+dy[k]][j+dx[k]]:
            return 1 + omok(i+dy[k], j+dx[k], k)
        else:
            return 1
    else:
        return 1
for i in range(19):
    for j in range(19):
        if board[i][j]: #알이 놓여있을 때
            for k in range(4):
                cnt = omok(i, j, k)
                if cnt == 5:
                    if omok(i+(4*dy[k]), j+(4*dx[k]), 7-k) == 5: #왔던길 돌아가면서 정확히 5개인지 확인
                        is_end = True
                        print(board[i][j])
                        print(i+1, j+1) # 실제 위치
if not is_end:
    print(0)