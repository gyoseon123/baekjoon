import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
        

start,end = map(int, input().split())

tracking = [i for i in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [INF]*(n+1)
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        if dis < distance[node]:
            continue
        for next,cost in enumerate(graph[node]):
            if cost == INF:
                continue
            if cost+distance[node] < distance[next]:
                distance[next] = cost+distance[node]
                tracking[next] = node
                heapq.heappush(q, (cost+distance[node], next))
    return distance

dis = dijkstra(start)[end]
result = []
now = end
while tracking[now] != now:
    result.append(now)
    now = tracking[now]
result.append(start)
result.reverse()
print(dis)
print(len(result))
print(*result)