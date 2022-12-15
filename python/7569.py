import sys
from collections import deque
m,n,h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)]for _ in range(h)]
tomato = deque()
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

for i in range(h):
    for j in range(n):
        for o in range(m):
            if graph[i][j][o] == 1:
                tomato.append([i,j,o])

def bfs():
    while tomato:
        x,y,z = tomato.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= 0 and nx < h and ny >= 0 and ny < n and nz >= 0 and nz < m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                tomato.append([nx,ny,nz])
def check(array):
    for i in range(h):
        for j in range(n):
            for o in range(m):
                if array[i][j][o] == 0:
                    return False
                if array[i][j][o] > max:
                    max = array[i][j][o]
    return max


bfs()
c = check(graph)
if c != False:
    print(c-1)
else:
    print(-1)
