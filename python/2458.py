import sys
input = sys.stdin.readline
n,m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF or graph[i][j] == 0:
            graph[i][j] = 0
        else:
            graph[i][j] = 1
            graph[j][i] = 1

cnt = 0
for i in graph[1:]:
    if sum(i[1:]) == n-1:
        cnt += 1
print(cnt)