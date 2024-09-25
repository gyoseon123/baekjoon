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
                trac[next] = now
                distance[next] = cost
                heapq.heappush(q, (cost, next))
                
    return distance
            

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
trac = [-1]*(n+1)

for _ in range(m):
    u,v,t = map(int, input().split())
    graph[u].append((v,t))
    graph[v].append((u,t))
    
min_path = set([1])
d1 = dijkstra(1)
if d1[n] == INF:
    print(-1)
    exit()


now = n
while True:
    min_path.add(now)
    now = trac[now]
    if now == 1:
        break
    
d2 = dijkstra(n)
ans = INF

for i in range(1, n+1):
    if i not in min_path:
        ans = min(ans, d1[i] + d2[i])

for i in list(min_path):
    for next, cst in graph[i]:
        if next in min_path and trac[i] != next and trac[next] != i:
            ans = min(ans, min(d1[i] + d2[next], d1[next] + d2[i]) + cst)

print(ans+d1[n] if ans != INF else -1)