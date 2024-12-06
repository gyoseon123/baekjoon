from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end, target):
    q = deque()
    q.append(start)
    visited = [False]*(n+1)
    visited[start] = True
    
    while q:
        now = q.popleft()
        
        for next, cst in graph[now]:
            if not visited[next] and cst >= target:
                visited[next] = True
                q.append(next)
    
    return visited[end]
    

n,m = map(int, input().split())
s,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,c = map(int, input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

left = 0
right = 1000001

while left + 1 < right:
    mid = (left+right)//2
    
    if bfs(s,e,mid):
        left = mid
    else:
        right = mid

print(left)