import sys
input = sys.stdin.readline

def find_point(time):
    ret = []
    
    for x,y,dx,dy in point:
        ret.append((x + dx*time, y + dy*time))
    
    return ret

def f(time):
    points = find_point(time)
    minx = sys.maxsize
    miny = sys.maxsize
    maxx = -sys.maxsize
    maxy = -sys.maxsize
    
    for x,y in points:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    
    return max(maxx - minx, maxy - miny)

n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]

lo = 0
hi = 2000

for _ in range(100000):
    p = (lo*2 + hi)/3
    q = (lo + hi*2)/3
    
    if f(p) >= f(q):
        lo = p
    else:
        hi = q

print(f(lo))
