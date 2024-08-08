import math
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
        
    return stk1 + list(reversed(stk2[1: len(stk2)-1]))

def find_line(x1, y1, x2, y2):
    if x1 - x2 == 0:
        return (1, 0, -x1)
    d = (y1 - y2)/(x1 - x2)
    return (d, -1, -d*x1 + y1)

def dist(line, x1, y1):
    a,b,c = line
    return abs(a*x1 + b*y1 + c)/((a*a + b*b)**0.5)

t = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    t += 1
    point = [tuple(map(int, input().split())) for _ in range(n)]
    ch = convex_hull(point)
 
    ans = int(1e9)
    for i in range(len(ch)):
        ret = 0
        fir = ch[i]
        sec = ch[(i+1)%len(ch)]
        line = find_line(*fir, *sec)
        for j in range(len(ch)):
            if j not in (i, (i+1)%len(ch)):
                ret = max(ret, dist(line, *ch[j]))
        ans = min(ans, ret)
    
    print(f"Case {t}: {math.ceil(ans*100)/100:.2f}")