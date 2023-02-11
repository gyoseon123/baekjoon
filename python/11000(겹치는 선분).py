import heapq
import sys
input = sys.stdin.readline
n = int(input())
lecture = []
for i in range(n):
    x,y = map(int, input().split())
    lecture.append((x,y))
lecture.sort()
q = []
heapq.heappush(q, lecture[0][1])
ans = len(q)
for x,y in lecture[1:]:
    while q and q[0] <= x:
        heapq.heappop(q)
    heapq.heappush(q, y)
    ans = max(ans, len(q))
print(ans)