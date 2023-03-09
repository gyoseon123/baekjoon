from collections import deque
import sys
input = sys.stdin.readline
n,m,x = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph1[b].append(a)
    graph2[a].append(b)

def bfs(node):
    visited = [False]*(n+1)
    visited[node] = True
    q = deque()
    q.append(node)
    cnt = 0
    while q:
        node = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] =  True
                q.append(next)
                cnt += 1
    return cnt

graph = graph1 #정방향 앞에 몇명이 있는가
print(1+bfs(x), end=" ")
graph = graph2 #역방향 뒤에 몇명이 있는가
print(n-bfs(x))