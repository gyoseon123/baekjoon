from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    global cnt
    graph[x][y] = 0
    cnt += 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 0 
            bfs(i,j)
            result.append(cnt)
if not result:
    print(0,0, sep='\n')
else:
    print(len(result), max(result), sep='\n')