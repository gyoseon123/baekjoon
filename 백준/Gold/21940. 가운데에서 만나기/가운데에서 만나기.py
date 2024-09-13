import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
    
for i in range(n+1):
    graph[i][i] = 0
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
k = int(input())
city = list(map(int, input().split()))
ans = []

for i in range(1, n+1):
    res = -1
    for j in range(k):
        res = max(res, graph[i][city[j]] + graph[city[j]][i])
    ans.append((res, i))

ans.sort()
print(ans[0][1], end=' ')
for i in range(1, len(ans)):
    if ans[i][0] == ans[0][0]:
        print(ans[i][1], end=' ')