from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x,t):
    q = deque()
    q.append((x,t))
    visited[x] = True
    while q:
        x,t = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                q.append((node,t+1))
                visited[node] = True
                distance[node] = t

result = []

for i in range(1,n+1):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    bfs(i,1)
    result.append(sum(distance))
m = min(result)
for i in range(n):
    if result[i] == m:
        print(i+1)
        break