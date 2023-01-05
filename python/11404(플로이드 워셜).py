import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in graph[1:]:
    for j in i[1:]:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()