import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF]*(n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dis, now = heapq.heappop(q)
        if dis > dist[now]: continue
        
        for next,c in graph[now]:
            cost = dist[now] + c
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))
    
    return dist

n,m = map(int, input().split())
p = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,c = map(int, input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

dist = dijkstra(1)
ans = 0
for i in range(1, n+1):
    ans += dist[i] * p[i]

print(ans)