from collections import deque
m,n = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(m)]
q = deque()
q.append([0,0])
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def dfs():
    while q:
        x,y = q.popleft()
        for i  in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
        
dfs()
print(graph[m-1][n-1])