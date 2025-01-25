import sys
input = sys.stdin.readline

def dfs(x,y,col):
    global cnt
    cnt += 1
    visit[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and not visit[nx][ny] and board[nx][ny] == col:
            dfs(nx, ny, col) 
    

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int, input().split())
board = [input().rstrip() for _ in range(m)]
visit = [[False]*n for _ in range(m)]

a,b = 0,0
for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            cnt = 0
            dfs(i,j,board[i][j])
            if board[i][j] == "W":
                a += cnt**2
            else:
                b += cnt**2

print(a,b)