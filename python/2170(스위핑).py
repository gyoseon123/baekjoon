import sys
input = sys.stdin.readline
n = int(input())
line = []
for i in range(n):
    line.append(tuple(map(int, input().split())))
line.sort()

INF = int(1e9)
l,r = -INF, -INF
ans = 0
for x,y in line:
    if x <= r:
        r = max(r, y)
    else:
        ans += r-l
        l,r = x,y
ans += r-l
print(ans)
        
