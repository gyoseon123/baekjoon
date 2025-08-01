# ai test

import sys
import heapq
input = sys.stdin.readline

N, E, K = map(int, input().split())
if K:
    voting_cities = set(map(int, input().split()))
else:
    voting_cities = set()
graph = [[] for _ in range(N)]
for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

Q = int(input())
queries = []
for _ in range(Q):
    arr = list(map(int, input().split()))
    S = arr[0]
    tickets = arr[1:]
    queries.append( (S, tickets) )

# 티켓 종류별 할인율
discount = [0, 0.1, 0.2, 0.3, 0.4, 0.5]  # ticket x, discount[x]

for query in queries:
    S, tickets = query

    # 32가지 티켓 구매 조합
    result = float('inf')
    for bitmask in range(32):
        use = []
        buy_cost = 0
        valid = True
        # 구매 조합 만들기
        for i in range(5):
            if (bitmask & (1 << i)):
                if tickets[i] == -1:
                    valid = False
                    break
                buy_cost += tickets[i]
                use.append(i+1)
        if not valid:
            continue
        # Dijkstra (state = (city, 티켓mask))
        heap = []
        dist = [ [float('inf')] * 32 for _ in range(N) ]
        start_ticketmask = 0  # 안 쓴 상태
        dist[S][start_ticketmask] = 0
        heapq.heappush(heap, (0, S, start_ticketmask))
        while heap:
            cost, u, tmask = heapq.heappop(heap)
            if dist[u][tmask] < cost:
                continue
            for v, c in graph[u]:
                # 티켓 안 씀
                if dist[v][tmask] > cost + c:
                    dist[v][tmask] = cost + c
                    heapq.heappush(heap, (cost + c, v, tmask))
                # 티켓 쓸 수 있으면
                for t in range(5):
                    if (bitmask & (1<<t)) and not (tmask & (1<<t)):
                        nc = c * (1 - discount[t+1])
                        ntmask = tmask | (1<<t)
                        nc = int(nc)  # 원래 비용 항상 10의 배수이므로, 정수
                        if dist[v][ntmask] > cost + nc:
                            dist[v][ntmask] = cost + nc
                            heapq.heappush(heap, (cost+nc, v, ntmask))
        # 각 투표도시까지의 최소 비용 + 티켓 구입비
        reach = False
        for t in voting_cities:
            for usemask in range(32):
                if dist[t][usemask] != float('inf'):
                    result = min(result, buy_cost + dist[t][usemask])
                    reach = True
        # 혹시 투표 도시 없음
    if not voting_cities or result == float('inf'):
        print(-1)
    else:
        print(result)
