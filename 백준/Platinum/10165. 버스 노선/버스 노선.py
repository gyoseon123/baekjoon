import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = []

for _ in range(m):
    s,e = map(int, input().split())
    if s > e:
        a.append((s-n, e, _))
        a.append((s, e+n, _))
    else:
        a.append((s, e, _))

a.sort(key = lambda x : (x[0], -x[1]))

ans = [1]*m
now = [a[0][0], a[0][1]]

for x, y, i in a[1:]:
    if y <= now[1]:
        ans[i] = 0
    else:
        now = [x,y]

print(*[i+1 for i in range(m) if ans[i]])