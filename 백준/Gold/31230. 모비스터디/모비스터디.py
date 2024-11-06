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
        c, now = heapq.heappop(q)
        if dist[now] < c: continue
        
        for next, cst in graph[now]:
            cost = dist[now] + cst
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))
        
    return dist

n,m,A,B = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

Adist = dijkstra(A)
Bdist = dijkstra(B)
min_dist = Adist[B]

ans = []
for i in range(1, n+1):
    if Adist[i] + Bdist[i] == min_dist:
        ans.append(i)

print(len(ans))
print(*ans)