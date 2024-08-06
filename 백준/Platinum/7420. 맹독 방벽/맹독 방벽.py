import math
import sys
input = sys.stdin.readline
PI = 3.141592653589793238462643383279502884197

def dist(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def convex_hull(points):
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

n,l = map(int, input().split())
point = [tuple(map(int, input().split())) for _ in range(n)]
point.sort()
ch = convex_hull(point)
ans = 0

for i in range(len(ch)-1):
    ans += dist(*ch[i], *ch[i+1])

ans += dist(*ch[0], *ch[len(ch)-1])
ans += 2*l*PI

print(int(ans+0.5))