import heapq
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
info = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(n):
    info.append((a[i], b[i]))

c.sort(reverse=True)

target = 0
ans = 0
for i in range(n):
    if info[i][0] <= c[target]:
        ans += (c[target] - info[i][0] + 1)%(info[i][0] - info[i][1])*2
    else:
        target += 1
    if target == m:
        break

print(ans)


