import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
p_1, p_2 = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
m = int(input())
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    q = deque()
    q.append((p_1, 0))
    while q:
        x, t = q.popleft()
        if x == p_2:
            return t
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append((i, t+1))

a = bfs()
if a == None:
    print(-1)
else:
    print(a)