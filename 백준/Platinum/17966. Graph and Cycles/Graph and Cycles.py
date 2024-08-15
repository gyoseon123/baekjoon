import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n*(n-1)//2):
    u,v,c = map(int, input().split())
    graph[u].append(c)
    graph[v].append(c)


for i in range(1, n+1):
    graph[i].sort()
    
ans = 0

for i in range(1, n+1):
    for j in range(0, n-1, 2):
        ans += max(graph[i][j], graph[i][j+1])

print(ans)