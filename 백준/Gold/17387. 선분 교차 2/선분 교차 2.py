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

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

print(1 if is_cross(p1, p2, p3, p4) else 0)