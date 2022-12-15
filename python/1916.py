import sys
import heapq
input = sys.stdin.readline
MAX = 10**9
n = int(input())
m = int(input())
distance = [MAX]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
city_start, city_end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, [0,start])
    distance[start] = 0
    while q:
        dis, end = heapq.heappop(q)
        if dis > distance[end]:
            continue
        for i in graph[end]:
            cost = distance[end] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


dijkstra(city_start)
print(distance[city_end])