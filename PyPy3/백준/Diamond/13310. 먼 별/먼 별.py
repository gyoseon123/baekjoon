import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x3 - x1)*(y2 - y1) - (y3 - y1)*(x2 - x1)

def dist_sq(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def convex_hull(points):
    points.sort()
    
    stk1 = []
    stk2 = []
    
    for point in points:
        while len(stk1) >= 2 and ccw(*stk1[-2], *stk1[-1], *point) >= 0: stk1.pop()
        while len(stk2) >= 2 and ccw(*stk2[-2], *stk2[-1], *point) <= 0: stk2.pop()
        stk1.append(point)
        stk2.append(point)
        
    return stk1 + list(reversed(stk2[1:len(stk2)-1]))

def find_point(x1, y1, x2, y2, x3, y3):
    return (x3 - x2 + x1, y3 - y2 + y1)

def find_max_dis(ch):
    r = 0
    ans = 0
    m = len(ch)
    for i in range(m):
        while (r < 2*m and ccw(*ch[i], *ch[(i+1)%m], *find_point(*ch[(i+1)%m], *ch[r%m], *ch[(r+1)%m])) <= 0):
            ans = max(ans, dist_sq(*ch[i], *ch[r%m]))
            r += 1
        ans = max(ans, dist_sq(*ch[i], *ch[r%m]))
    
    return ans
    
def f(d):
    ret = []
    for i in range(n):
        ret.append((point[i][0] + point[i][2]*d, point[i][1] + point[i][3]*d))
    
    ch = convex_hull(ret)
    return find_max_dis(ch)

n,t = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(n)]

lo = 0
hi = t

while hi - lo >= 3:
    p = (lo*2 + hi)//3 
    q = (lo + hi*2)//3
    
    if f(p) <= f(q): hi = q
    else: lo = p
    
ans = sys.maxsize
idx = -1
for i in range(lo, hi+1):
    v = f(i)
    if v < ans:
        idx = i
        ans = v

print(idx)
print(ans)
        
        