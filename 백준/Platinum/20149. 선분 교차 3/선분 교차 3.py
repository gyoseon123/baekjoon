import sys
input = sys.stdin.readline
INF = sys.maxsize

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

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

def find_line(x1, y1, x2, y2):
    if x1 - x2 == 0:
        return (1, 0, -x1)
    d = (y1 - y2)/(x1 - x2)
    return (d, -1, -d*x1 + y1)

def find_point(line1, line2):
    a1,b1,c1 = line1
    a2,b2,c2 = line2
    x = (c1*b2 - c2*b1)/(a2*b1 - b2*a1)
    if b1 == 0:
        return (x, (-c2 - a2*x)/b2)
    y = (-c1 - a1*x)/b1
    return (x,y)

def tan(x1, y1, x2, y2):
    if x1 - x2 == 0:
        return INF
    
    return (y1 - y2)/(x1 - x2)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

if is_cross(p1, p2, p3, p4):
    print(1)
else:
    print(0)
    exit()

d1 = tan(*p1, *p2)
d2 = tan(*p3, *p4)

if d1 == d2:
    if p2 > p1:
        p1, p2 = p2, p1
    if p4 > p3:
        p3, p4 = p4, p3
    
    if p2 == p3:
        print(*p2)
    elif p1 == p4:
        print(*p1)
    else:
        pass
else:
    print(*find_point(find_line(*p1, *p2), find_line(*p3, *p4)))
