import heapq
import sys
input = sys.stdin.readline
n = int(input())
line = []
for i in range(n):
    x,y = map(int, input().split())
    line.append((x,y))
line.sort()
q = []
heapq.heappush(q, line[0][1])
ans = 1
for x,y in line[1:]:
    while q and q[0] <= x:
        heapq.heappop(q)
    heapq.heappush(q, y)
    ans = max(ans, len(q))
print(ans)

