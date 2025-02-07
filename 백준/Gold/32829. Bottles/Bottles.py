import heapq
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [[0] + list(map(int, input().split())) for _ in range(n)]
l = [0]*m

for i in range(n):
    for j in range(m):
        board[i][j+1] += board[i][j]

for j in range(m):
    q = []
    lines = []
    ans = 0
    for i in range(n):
        lines.append((board[i][j], board[i][j+1]))
    lines.sort()
    for x,y in lines:
        heapq.heappush(q, y)
        while q and q[0] <= x:
            heapq.heappop(q)
        ans = max(ans, len(q))
    l[j] = ans

print(*l)