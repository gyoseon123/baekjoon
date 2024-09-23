import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    trac = [[] for _ in range(n+1)]
    dist = [INF]*(n+1)
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
    
    rett = [[] for _ in range(n+1)]
    for i in range(n+1):
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
                graph[now].remove([next, edge[1]])
                break
        if not visited[next]:
            dfs(next)


n,m,s,d = map(int, input().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,p = map(int, input().split())
    graph[u].append([v,p])
    graph[v].append([u,p])

fir_d = dijkstra(s)
trac = fir_d[0]
visited = [False]*(n+1)
dfs(d)

ans = 0
for l in graph:
    if l: ans += sum([i[1] for i in l])

print(ans//2)