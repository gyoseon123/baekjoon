from functools import cmp_to_key
import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def compare(p1, p2):
    dir = ccw(*point[0], *p1, *p2)
    return (dir < 0) - (dir > 0)

n = int(input())

point = []
for _ in range(n):
    x,y,c = input().split()
    if c == "Y":
        point.append((int(x), int(y)))
    
point.sort()
point[1:] = sorted(point[1:], key=cmp_to_key(compare))

index = len(point)-1
cnt = 1
for i in range(index, -1, -1):
    if ccw(*point[0], *point[i], *point[i-1]) == 0:
        cnt += 1
    else:
        break


if cnt:
    point[len(point) - cnt:] = reversed(point[len(point) - cnt:])

print(len(point))
for x,y in point:
    print(x,y)