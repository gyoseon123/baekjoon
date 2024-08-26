import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x3 -x1)*(y2 - y1) - (y3 -y1)*(x2 - x1)

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
        

n,m = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]

point = []

for i in range(n):
    for j in range(m):
        point.append((a[i][0] + b[j][0], a[i][1] + b[j][1]))

ch = convex_hull(point)

print(len(ch))
for x,y in ch:
    print(x,y)