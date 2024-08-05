import math
import sys
input = sys.stdin.readline

def slope(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)

n = int(input())
l = list(map(int, input().split()))
point = []

for i in range(n):
    point.append((i+1, l[i]))

ans = 0

for i in range(n):
    max_slope = -int(1e9)
    cnt = 0
    for j in range(i+1, n):
        if slope(*point[i], *point[j]) > max_slope:
            max_slope = slope(*point[i], *point[j])
            cnt += 1
    
    min_slope = int(1e9)
    for j in range(i-1, -1, -1):
        if slope(*point[j], *point[i]) < min_slope:
            min_slope = slope(*point[j], *point[i])
            cnt += 1
            
    ans = max(ans, cnt)

print(ans)
        