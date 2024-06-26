import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
V,E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w)) # u -> v 가중치 w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        for next in graph[node]:
            if next[1]+distance[node] < distance[next[0]]:
                distance[next[0]] = next[1]+distance[node]
                heapq.heappush(q, (next[1]+distance[node],next[0]))

dijkstra(K)

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)