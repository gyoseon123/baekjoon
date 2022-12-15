import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def dfs(x,y):
    if graph[x][y] == 0:
        graph[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                dfs(nx,ny)

def check_cheese():
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if graph[nx][ny] == 2:
                        cnt += 1
                if cnt >= 1:
                    result.append([i,j])
    return result
dfs(0,0)
cnt = 0
while True:
    l = check_cheese()
    if not l:
        break
    temp = len(l)
    cnt += 1
    for i in l:
        x,y = i[0], i[1]
        graph[x][y] = 0
        dfs(x,y)
print(cnt, temp, sep = '\n')


