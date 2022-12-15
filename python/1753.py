import sys
import heapq
input = sys.stdin.readline
V,E = map(int, input().split())
K = int(input())
INF = int(1e9)
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for i in range(E):
    u,v,w = map(int, input().split()) # u 에서 v로 w만큼
    graph[u].append([v,w])

def dijkstra(start):
    q = []
    heapq.heappush(q, [0,start])
    distance[start] = 0
    while q:
        dis, end = heapq.heappop(q)
        if distance[end] < dis:
            continue
        for i in graph[end]:
            cost = distance[end] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])




dijkstra(K)
for i in range(1,V+1):
    if distance[i] == int(1e9):
        print('INF')
    else:
        print(distance[i])    

