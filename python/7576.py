from collections import deque
m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

def check_zero(array):
    max = 0
    sig = False
    for i in range(n):
        for j in range(m):
            if array[i][j] > max:
                max = array[i][j]
            if array[i][j] == 0:
                sig = True
    if sig != True:
        return max
    else:
        return False

bfs()

c = check_zero(graph)
if c != False:
    print(c-1)
else:
    print(-1)