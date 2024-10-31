import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
stage = [tuple(map(int, input().split())) for _ in range(n)]

q = []
star = 0
ans = 0

while True:
    while q and q[0] <= star:
        star += 1
        ans += 1
        heapq.heappop(q)
    
    maxb = -1
    idx = -1
    flg = False
    
    for i in range(len(stage)):
        nowa, nowb = stage[i]
        if nowb <= star:
            flg = True
            star += 2
            ans += 1
            del stage[i]
            break
        if nowa <= star and nowb > maxb:
            idx = i
            maxb = nowb
    else:
        if maxb != -1:
            flg = True
            star += 1
            ans += 1
            heapq.heappush(q, maxb)
            del stage[idx]
    
    if not flg: break

print(ans if not any([q, stage]) else "Too Bad")