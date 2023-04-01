import sys
input = sys.stdin.readline
r,c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[False]*c for _ in range(r)]

def dfs(x,y):
    global v_cnt, o_cnt
    if graph[x][y] == "o":
        o_cnt += 1
    if graph[x][y] == "v":
        v_cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c and not visited[nx][ny]:
            if graph[nx][ny] != "#": 
                dfs(nx,ny)
            

v = 0
o = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != "#":
            v_cnt = 0
            o_cnt = 0
            dfs(i,j)
            if v_cnt >= o_cnt:
                v += v_cnt
            else:
                o += o_cnt
    
print(o,v)


