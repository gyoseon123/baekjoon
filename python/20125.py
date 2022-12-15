import sys
input = sys.stdin.readline
n = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
board = [list(input().rstrip()) for _ in range(n)]
for x in range(n):
    for y in range(n):
        if board[x][y] == '*':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if board[nx][ny] != '*':
                    break
            else:
                center_x, center_y = x,y

min_ = n
max_ = 0
for i in range(n):
    
            

