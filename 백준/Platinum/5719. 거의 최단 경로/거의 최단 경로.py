import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    trac = [[] for _ in range(n)]
    dist = [INF]*n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        c, now  = heapq.heappop(q)
        if c > dist[now]: continue

        for next, cst in graph[now]:
            cost = cst + c
            if cost < dist[next]:
                dist[next] = cost
                trac[next].append((cost, now))
                heapq.heappush(q, (cost, next))
            if cost == dist[next]:
                trac[next].append((cost, now))
    
    rett = [[] for _ in range(n)]
    for i in range(n):
        if not trac[i]: continue

        min_cst = min([j[0] for j in trac[i]])
        for cst, node in trac[i]:
            if cst == min_cst: rett[i].append(node)

    
    return (rett, dist[d])

def dfs(now):
    visited[now] = True
    for next in trac[now]:
        for edge in graph[next]:
            if edge[0] == now:
                graph[next].remove(edge)
                break
        if not visited[next]:
            dfs(next)

while True:
    n,m = map(int, input().split())
    if (n,m) == (0,0): break

    s,d = map(int, input().split())
    
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u,v,p = map(int, input().split())
        graph[u].append([v,p])
    
    fir_d = dijkstra(s)
    trac = fir_d[0]
    visited = [False]*n

    for arr in trac:
        arr = list(set(arr))

    dfs(d)
    dist = dijkstra(s)[1]

    print(dist if dist != INF else -1)