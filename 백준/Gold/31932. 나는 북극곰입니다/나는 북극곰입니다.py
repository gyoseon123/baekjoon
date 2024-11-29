import heapq
import sys
input = sys.stdin.readline

INF = int(1e12)

def dijkstra(start, t):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start, 0))
    distance[start] = 0
    while q:
        dis, now, time = heapq.heappop(q)
        
        if distance[now] < dis:
            continue
        
        for next in graph[now]:
            cost = dis + next[0]
            if cost < distance[next[1]] and cost <= next[2] - t:
                distance[next[1]] = cost
                heapq.heappush(q, (cost, next[1], next[2]))
    if distance[n] != INF:
        return True
    else:
        return False


n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,d,t = map(int, input().split())
    graph[u].append((d,v,t))
    graph[v].append((d,u,t))

left = -1
right = int(1e12)+1

while left + 1 < right:
    mid = (left+right)//2
    
    if dijkstra(1, mid):
        left = mid
    else:
        right = mid

print(left)
        
