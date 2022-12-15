n,m,r = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
print(graph)
for i in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1

def dfs(r):
    if visited[r] == 0:
        print(r)
        visited[r] = 1
        for i in range(1,n+1):
            if graph[r][i] == 1:
                dfs(i)
dfs(r)
                

