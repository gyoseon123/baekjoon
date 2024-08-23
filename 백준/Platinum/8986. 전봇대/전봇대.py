import sys
input = sys.stdin.readline

def f(itv):
    now = 0
    ret = 0
    for i in range(1, n):
        now += itv
        ret += abs(l[i] - now)
    
    return ret 
        
n = int(input())
l = list(map(int, input().split()))

lo = 0
hi = int(1e9)

while hi - lo >= 3:
    p = (lo*2 + hi)//3
    q = (lo + hi*2)//3
    
    if f(p) >= f(q):
        lo = p
    else:
        hi = q
    
ans = sys.maxsize
for i in range(lo, hi+1):
    ans = min(ans, f(i))

print(ans)
    