import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def convex_hull():
    stk1 = []
    stk2 = []
    for x,y in point:
        while len(stk1) >= 2:
            dir = ccw(*stk1[-2], *stk1[-1], x, y)
            if dir >= 0:
                stk1.pop()
            else:
                break
                
        while len(stk2) >= 2:
            dir = ccw(*stk2[-2], *stk2[-1], x, y)
            if dir <= 0:
                stk2.pop()
            else:
                break
                
        stk1.append((x,y))
        stk2.append((x,y))
        
    return (set(stk1)|set(stk2))
    
    


n,px,py = map(int, input().split())
point = [tuple(map(int, input().split())) for _ in range(n)]
point.append((px, py))
point.sort()

ans = 0
while True:
    ch = convex_hull()
    if (px, py) in ch or len(ch) <= 2:
        break
    ans += 1
    point = sorted(list(set(point)^ch))

print(ans)