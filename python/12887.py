from collections import deque
import sys
input = sys.stdin.readline
m = int(input())
graph = [list(input().rstrip()) for _ in range(2)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
white_cnt = 0
for i in range(2):
    for j in range(m):
        if graph[i][j] == '.':
            white_cnt += 1
if m == 1:
    print(white_cnt-1)
    exit()

def bfs(x,y):
    q = deque()
    visited = [[False]*m for _ in range(2)]
    q.append((x,y,1))
    visited[x][y] = True
    while q:
        x,y,dis = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < 2 and ny >= 0 and ny < m:
                if not visited[nx][ny] and graph[nx][ny] == '.':
                    if ny == m-1:
                        return dis+1
                    visited[nx][ny] = True
                    q.append((nx,ny,dis+1))
result = []
if graph[0][0] == '.':
    result.append(white_cnt - bfs(0,0))
if graph[1][0] == '.':
    result.append(white_cnt - bfs(1,0)) 
print(max(result))