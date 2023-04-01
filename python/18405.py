from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s,sx,sy = map(int, input().split())
virus = [[] for _ in range(k+1)]
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus[graph[i][j]].append((i,j))
            visited[i][j] = True

nq = []
q = deque()
for l in virus:
    for i,j in l:
        nq.append((i,j))
q.append(nq)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(s):
    next_q = []
    virus_list = q.popleft()
    for x,y in virus_list:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny]:
                    graph[nx][ny] = graph[x][y]
                    visited[nx][ny] = True
                    next_q.append((nx,ny))
    if not next_q:
        break
    q.append(next_q)

print(graph[sx-1][sy-1])