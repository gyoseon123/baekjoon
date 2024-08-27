import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)

def convex_hull(coordinates, cw):
    stk = []
    for point in coordinates:
        while len(stk) >= 2:
            dir = ccw(*stk[-2], *stk[-1], *point)
            if dir == 0 or (dir > 0)^cw:
                stk.pop()
            else:
                break
        stk.append(point)

    return len(stk)

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()

print(convex_hull(l, 0) + convex_hull(l, 1) - 2)   






