import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        dis, now = heapq.heappop(q)
        
        if dis > dist[now]: continue
        
        for next, c in graph[now]:
            cost = c + dist[now]
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (dist[next], next))
    
t = int(input())

for _ in range(t):
    n,d,c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF]*(n+1)
    for i in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a,s))
    
    dijkstra(c)
    
    cnt = 0
    ans = 0
    
    for i in range(1, n+1):
        if dist[i] != INF:
            cnt += 1
            ans = max(ans, dist[i])
    
    print(cnt, ans)
    
