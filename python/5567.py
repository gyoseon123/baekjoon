from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    q = deque()
    q.append((1,0)) # 시작정점, 탐색 범위
    visited[1] = True
    while q:
        x,t = q.popleft()
        for node in graph[x]:
            if not visited[node] and t < 2:
                visited[node] = True
                q.append((node, t+1))
bfs()
print(visited.count(True)-1)