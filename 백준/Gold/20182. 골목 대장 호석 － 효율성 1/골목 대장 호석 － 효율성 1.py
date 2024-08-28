import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    distance = [INF]*(n+1)
    
    heapq.heappush(q, (0, 0, start))
    distance[start] = 0
    
    ret = INF
    
    while q:
        dis, now_max, now = heapq.heappop(q)
            
        if dis > c: continue
        
        if now == b:
            ret = min(ret, now_max)
        
        for next, cst in graph[now]:
            cost = dis + cst
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, max(now_max, cst), next))
                
    return ret

n,m,a,b,c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,cst = map(int, input().split())
    graph[u].append((v, cst))
    graph[v].append((u, cst))


d = dijkstra(a)
print(d if d != INF else -1)