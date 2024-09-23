import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dis, now = heapq.heappop(q)
        
        if dis > distance[now]: continue
        
        for next, cst in graph[now]:
            cost = cst + distance[now]
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    
    return distance


n,m,a,b = map(int, input().split())
graph = [[] for _ in range(n+1)]
edges = []

for _ in range(m):
    u,v,c = map(int, input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))
    edges.append((u,v,c))
    
d1 = dijkstra(a)
d2 = dijkstra(b)

ans = 0
min_c = d1[b]

for u,v,c in edges:
    if d1[v] + d2[u] + c == min_c or d1[u] + d2[v] + c == min_c: continue
    ans += c

print(ans)