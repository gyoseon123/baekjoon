import sys
input = sys.stdin.readline

n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
point_set = set(point)

ans = 0
for i in range(n):
    for j in range(n):
        if i == j: continue
        
        p1 = point[i]
        p2 = point[j]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if ((p1[0] - dy, p1[1] + dx) in point_set) and ((p2[0] - dy, p2[1] + dx) in point_set): ans += 1

print(ans//4)