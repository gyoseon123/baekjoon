# import sys
# input = sys.stdin.readline
# n,m,r = map(int, input().split())
# t = list(map(int, input().split()))
# INF = int(1e9)
# graph = [[INF]*(n+1) for _ in range(n+1)]
# for _ in range(r):
#     a,b,l = map(int, input().split())
#     graph[a][b] = l
#     graph[b][a] = l

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             graph[i][j] = 0

# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# result = 0
# for line in graph[1:]:
#     cost = 0
#     for area in range(1,len(line)):
#         if line[area] <= m:
#             cost += t[area-1]
#     result = max(result, cost)
# print(result) 


import heapq
import sys
input = sys.stdin.readline
n,m,r = map(int, input().split())
t = [0] + list(map(int, input().split()))

INF = int(1e9)
graph = [[]*(n+1) for _ in range(n+1)]

for i in range(r):
    a,b,l = map(int, input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))
def dijkstra(v):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,v))
    distance[v] = 0
    while q:
        dis,node = heapq.heappop(q)
        if dis > distance[node]: continue
        if distance[node] > m: continue

        for next in graph[node]:
            cost = next[1] + dis
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    result = 0
    for i in range(1,n+1):
        if distance[i] <= m:
            result += t[i]
    return result

result = 0
for i in range(1,n+1):
    result = max(result, dijkstra(i))
print(result)