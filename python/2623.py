from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
indgree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    l = list(map(int, input().split()))
    for i in range(1,len(l)-1):
        graph[l[i]].append(l[i+1])
        indgree[l[i+1]] += 1

q = deque()
result = []
for i in range(1,n+1):
    if indgree[i] == 0:
        q.append(i)
while q:
    node = q.popleft()
    result.append(node)
    for i in graph[node]:
        indgree[i] -= 1
        if indgree[i] == 0:
            q.append(i)
if len(result) == n:
    print(*result, sep='\n')
else:
    print(0)