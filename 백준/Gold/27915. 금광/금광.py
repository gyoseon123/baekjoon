from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    dist = [-1]*(n+1)
    dist[start] = 0
    q = deque()
    q.append((start, 0))

    while q:
        now, dis = q.popleft()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dis + 1
                q.append((next, dis+1))
    
    return dist
    

n = int(input())
a = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    graph[a[i]].append(i+2)

b = bfs(1)

odd = 0
even = 0

for i in range(1, n+1):
    if b[i]&1: odd += 1
    else: even += 1

print(max(odd, even))