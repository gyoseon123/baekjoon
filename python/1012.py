import sys
sys.setrecursionlimit(10000)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False 
    if graph[x][y] == 1: 
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i],y + dy[i])
        return True
    return False

    




t = int(sys.stdin.readline())
for i in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt += 1
    print(cnt)