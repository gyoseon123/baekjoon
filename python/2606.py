def dfs(x):
    global cnt
    if visited[x] == 0:
        visited[x] = 1
        cnt += 1
        for i in range(n+1):
            if graph[x][i] == 1:
                graph[x][i] = 0
                graph[i][x] = 0
                dfs(i)

cnt = 0
n = int(input())
a = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(a):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
dfs(1)
print(cnt-1)