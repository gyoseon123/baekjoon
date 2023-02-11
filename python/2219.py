import sys
input = sys.stdin.readline
n,m = map(int, input().split())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]


for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

num = INF
computer = 0
for i in range(1,n+1):
    if sum(graph[i][1:]) < num:
        computer = i
        num = sum(graph[i][1:])

print(computer)


