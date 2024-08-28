import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, target):
    q = []
    distance = [INF]*(n+1)
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dis, now = heapq.heappop(q)
        
        for next, cst in graph[now]:
            if cst > target: continue
            
            cost = dis + cst
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost,  next))
            
    return distance[b]

n,m,a,b,c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,cst = map(int, input().split())
    graph[u].append((v, cst))
    graph[v].append((u, cst))

left = 0
right = 21

while left + 1 < right:
    mid = (left + right)//2
    
    if dijkstra(a, mid) <= c:
        right = mid
    else:
        left = mid

print(right if right != 21 else -1)
