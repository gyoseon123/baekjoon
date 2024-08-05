import sys
input = sys.stdin.readline

def dist_sq(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

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

def find_point(x1, y1, x2, y2, x3, y3): # ch[i+1], ch[r], ch[r+1]
    return (x3 - x2 + x1, y3 - y2 + y1)

n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]

ch = convex_hull(point)

r = 0
ans = 0
m = len(ch)
for i in range(m):
    while (r < 2*m and ccw(*ch[i], *ch[(i+1)%m], *find_point(*ch[(i+1)%m], *ch[r%m], *ch[(r+1)%m])) <= 0):
        ans = max(ans, dist_sq(*ch[i], *ch[r%m]))
        r += 1
    ans = max(ans, dist_sq(*ch[i], *ch[r%m]))

print(ans)