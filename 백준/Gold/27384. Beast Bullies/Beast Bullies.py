import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

l.sort(reverse=True)

target = l[0]
now = 0
ans = 1

for i in range(1, n):
    now += l[i]
    if now >= target:
        target = target + now
        ans = i+1
        now = 0

print(ans)