import sys
input = sys.stdin.readline

n = int(input())
x,s = map(int, input().split())

max_dmg = 0
for _ in range(n):
    c,p = map(int, input().split())
    if c <= x:
        max_dmg = max(max_dmg, p)

if max_dmg >= s:
    print("YES")
else:
    print("NO")