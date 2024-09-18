import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now):
    visited[now] = True
    
    for next in graph[now]:
        if not visited[next]:
            dfs(next)

n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(1, m+1):
    u,v = map(int, input().split())
    if i == k:
        node1 = u
        node2 = v
    else:
        graph[u].append(v)
        graph[v].append(u)

visited = [False]*(n+1)
dfs(node1)
set1 = set()
for i in range(1, n+1):
    if visited[i]:
        set1.add(i)

visited = [False]*(n+1)
dfs(node2)
set2 = set()
for i in range(1, n+1):
    if visited[i]:
        set2.add(i)

print(len(set1 - (set1&set2)) * len(set2 - (set1&set2)))