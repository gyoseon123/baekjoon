import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m = map(int, input().split())
graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y,a,b = map(int, input().split())
    graph[x][y].append((a,b))
visited = [[False]*(n+1) for _ in range(n+1)]
light = [[False]*(n+1) for _ in range(n+1)]
cnt = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def find_path(x,y):
    result = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 1 and nx < n+1 and ny >= 1 and ny < n+1:
            result.append((nx,ny))
    return result


def dfs(x,y):
    global cnt
    visited[x][y] = True
    for a,b in graph[x][y]:
        if not light[a][b]:
            light[a][b] = True
            cnt += 1
            for nx,ny in find_path(a,b):
                if visited[nx][ny]:
                    dfs(a,b)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 1 and nx < n+1 and ny >= 1 and ny < n+1:
            if not visited[nx][ny] and light[nx][ny]:
                dfs(nx,ny)
    
light[1][1] = True
dfs(1,1)
print(cnt+1)

