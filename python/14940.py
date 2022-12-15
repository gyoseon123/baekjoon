import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append([i,j])
            visited[i][j] = 1

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0: 
                if graph[nx][ny] == 0:
                    pass
                else:
                    visited[nx][ny] = 1
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx,ny])

bfs()
for i in range(n):
    for j in range(m):
        x = graph[i][j]
        if x == 1:
            graph[i][j] = -1
        elif x != 0:
            graph[i][j] -= 2

for i in graph:
    for j in i:
        print(j, end = ' ')
    print()