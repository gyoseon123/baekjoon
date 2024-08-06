import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def convex_hull(points):
    points.sort()
    stk1 = []
    stk2 = []
    for point in points:
        while len(stk1) >= 2:
            if ccw(*stk1[-2], *stk1[-1], *point) >= 0:
                stk1.pop()
            else:
                break
            
        while len(stk2) >= 2:
            if ccw(*stk2[-2], *stk2[-1], *point) <= 0:
                stk2.pop()
            else:
                break
        
        stk1.append(point)
        stk2.append(point)
        
    return stk1 + list(reversed(stk2[1:len(stk2)-1]))

def is_in(convex_hull, point):
    cnt = 0
    for i in range(len(convex_hull)):
        dir = ccw(*convex_hull[i], *convex_hull[(i+1)%len(convex_hull)], *point)
        if dir < 0:
            cnt += 1
        if dir == 0:
            points = list(sorted([convex_hull[i], convex_hull[(i+1)%len(convex_hull)], point]))
            if points.index(point) == 1:
                cnt += 1
            
    return cnt == len(convex_hull)

def is_cross(p1, p2, p3, p4):
    dir1 = ccw(*p1, *p2, *p3)*ccw(*p1, *p2, *p4)
    dir2 = ccw(*p3, *p4, *p1)*ccw(*p3, *p4, *p2)
    
    if (dir1, dir2) == (0,0):
        if p2 > p1:
            p1, p2 = p2, p1
        if p4 > p3:
            p3, p4 = p4, p3
        
        return (p3 <= p2 and p1 <= p4) or (p2 <= p3 and p4 <= p1)
    
    return dir1 <= 0 and dir2 <= 0

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    point = [tuple(map(int, input().split())) for _ in range(n+m)]
    white = [point[i] for i in range(n)]
    black = [point[i] for i in range(n, n+m)]
    wch = convex_hull(white)
    bch = convex_hull(black)
    
    in_point = False
    
    if len(wch) >= 2:
        for point in black:
            in_point |= is_in(wch, point)
    if len(bch) >= 2:
        for point in white:
            in_point |= is_in(bch, point)
    
    if len(bch) == 2 and len(wch) == 2:
        print("NO" if is_cross(*wch, *bch) else "YES")
    else:
        print("NO" if in_point else "YES")
        