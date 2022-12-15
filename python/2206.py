from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
break_wall = []
for i in range(n):
    for j in range(m):
        cnt = 0
        if graph[i][j] == 1:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                    cnt += 1
            if cnt >= 2:
                break_wall.append((i,j))

def bfs():
    q = deque()
    q.append((0,0,-1))
    graph[0][0] = -1
    while q:
        x,y,d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = d-1
                q.append((nx,ny,d-1))

result = []

for x,y in break_wall:
    temp = [i[:] for i in graph]
    graph[x][y] = 0
    bfs()
    if graph[n-1][m-1] != 0:
        result.append(-graph[n-1][m-1])
    graph = [i[:] for i in temp]
if not result:
    print(-1)
else:
    print(min(result))
