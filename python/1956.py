import sys
input = sys.stdin.readline
V,E = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(V+1) for _ in range(V+1)]
for i in range(E):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for i in range(1,V+1):
    graph[i][i] = 0

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = INF
for i in range(1,V+1):
    for j in range(1,V+1):
        if i == j:
            continue
        if graph[i][j] != INF and graph[j][i] != INF:
            result = min(result, graph[i][j] + graph[j][i])

if result == INF:
    print(-1)
else:
    print(result)