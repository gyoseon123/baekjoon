import sys
input = sys.stdin.readline

n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]

point.sort()

left = [0]*(n+1)
mid = [0]*(n+1)
right = [0]*(n+1)

for i in range(n):
    typ = point[i][1]
    if typ == -1: left[i+1] = 1
    elif typ == 1: right[i+1] = 1
    else: mid[i+1] = 1

for i in range(n):
    left[i+1] += left[i]
    right[i+1] += right[i]
    mid[i+1] += mid[i]

ans = 0

for i in range(n):
    typ = point[i][1]
    if typ == -1:
        ans += right[i]
        ans += mid[i]*2
    elif typ == 1:
        ans += (mid[n] - mid[i+1])*2

print(ans)