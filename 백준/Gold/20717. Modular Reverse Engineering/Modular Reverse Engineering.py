import sys
input = sys.stdin.readline

v,x,m = map(int, input().split())

res = []
for q in range(1, 1000000):
    p = (v*q)%m
    if p == 0 and v != 0:
        continue
    if x*q <= p < (x + 1)*q:
        res.append((p,q))

if not res:
    print(-1)
else:
    res.sort()
    print(*res[0])