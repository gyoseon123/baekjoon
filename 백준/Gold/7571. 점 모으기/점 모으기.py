import sys
input = sys.stdin.readline

def f1(v):
    ret = 0
    for i in range(m): ret += abs(v - point[i][0])
    return ret
    
def f2(v):
    ret = 0
    for i in range(m): ret += abs(v - point[i][1])
    return ret

n,m = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(m)]

lo = 0
hi = n+1

ans = 0
while hi - lo >= 3:
    p = (lo*2 + hi)//3
    q = (lo + hi*2)//3
    
    if f1(p) >= f1(q):
        lo = p
    else:
        hi = q
    
mn = int(1e18)
for i in range(lo, hi+1):
    mn = min(mn, f1(i))

ans += mn

lo = 0
hi = n+1
while hi - lo >= 3:
    p = (lo*2 + hi)//3
    q = (lo + hi*2)//3
    
    if f2(p) >= f2(q):
        lo = p
    else:
        hi = q
    
mn = int(1e18)
for i in range(lo, hi+1):
    mn = min(mn, f2(i))

ans += mn

print(ans)