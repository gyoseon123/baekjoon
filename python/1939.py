from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start, end = map(int, input().split())

def bfs(w):
    q = deque()
    visited = [False]*(n+1)
    q.append(start)
    while q:
        now = q.popleft()
        for node, weight in graph[now]:
            if not visited[node] and weight >= w:
                if node == end:
                    return True
                visited[node] = True
                q.append(node)
    return False

left = 0
right = 1000000000
while left <= right:
    mid = (left+right)//2
    is_able = bfs(mid)
    if is_able:
        left = mid+1
    else:
        right = mid-1

print((left+right)//2)