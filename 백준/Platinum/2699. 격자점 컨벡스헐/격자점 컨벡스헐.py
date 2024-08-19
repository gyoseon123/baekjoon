import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x3 - x1)*(y2 - y1) - (y3 - y1)*(x2 - x1)

def convex_hull(points):
    points.sort()
    stk1 = []
    stk2 = []
    for point in points:
        while len(stk1) >= 2 and ccw(*stk1[-2], *stk1[-1], *point) <= 0:
            stk1.pop()
        while len(stk2) >= 2 and ccw(*stk2[-2], *stk2[-1], *point) >= 0:
            stk2.pop()
        
        stk1.append(point)
        stk2.append(point)
    return stk1 + list(reversed(stk2[1:len(stk2)-1]))
        

p = int(input())

for _ in range(p):
    n = int(input())
    point = []
    for i in range((n+4)//5):
        l = list(map(int, input().split()))
        for j in range(0, len(l), 2):
            point.append((-l[j+1], l[j]))
    
    ch = convex_hull(point)
    print(len(ch))
    for x,y in ch:
        print(y,-x)