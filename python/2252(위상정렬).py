from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indgree = [0]*(n+1)
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    indgree[y] += 1

result = []
q = deque()
for i in range(1,n+1):
    if indgree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indgree[i] -= 1
        if indgree[i] == 0:
            q.append(i)

print(*result)

