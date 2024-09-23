import heapq
import sys
input =  sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    distance = [INF]*n
    distance[s] = 0
    q = []
    heapq.heappush(q, (0, 0, s))
    
    while q:
        dis, cst, now = heapq.heappop(q)
        
        for next, d, c in graph[now]:
            cost = dis + d
            if cost < distance[next] and c + cst <= r:
                distance[next] = cost
                heapq.heappush(q, (cost, c + cst, next))
    
    return distance
                

while True:
    try:
        n,m = map(int, input().split())
    except:
        break
    
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v,t,c = map(int, input().split())
        graph[u].append((v,t,c))
        graph[v].append((u,t,c))
    
    s,d,r = map(int, input().split())
    
    print(dijkstra()[d])
