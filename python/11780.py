import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
route = [[[0]]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
        route[a][b] = [a,b]

for i in range(1,n+1):
    graph[i][i] = 0
    route[i][i] = [0]

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                route[i][j] = route[i][k][:len(route[i][k])-1] + route[k][j]

for i in graph[1:]:
    for j in i[1:]:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()

for i in route[1:]:
    for j in i[1:]:
        if len(j) == 1:
            print(*j)
        else:
            print(len(j),*j)