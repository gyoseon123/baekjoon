from collections import defaultdict
import math
import heapq
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
board = [[-1]*n for _ in range(n)]

board[0][0] = a[0]

ans = [-1]*n
ans[0] = math.isqrt(a[0])

pq = []
for num in a[1:]:
    heapq.heappush(pq, num)

d = defaultdict(int)

for i in range(1, n):
    ans[i] = pq[0]//ans[0]
    
    board[i][0] = pq[0]
    board[0][i] = pq[0]
    d[pq[0]] += 2
    
    for j in range(1, i+1):
        board[i][j] = ans[i] * ans[j]
        board[j][i] = board[i][j]
        if i != j: d[board[i][j]] += 2
        else: d[board[i][j]] += 1

    while pq and d[pq[0]]:
        d[heapq.heappop(pq)] -= 1

flg = 1
d1 = defaultdict(int)
d2 = defaultdict(int)

for i in range(n):
    for j in range(n):
        d1[ans[i]*ans[j]] += 1

for num in a:
    d2[num] += 1

for key, val in d1.items():
    if key not in d2: flg = 0
    else:
        if val != d2[key]: flg = 0

if flg:
    print("YES")
    for i in range(n):
        print(ans[i], end=' ')
else:
    print("NO")