import sys
input = sys.stdin.readline

j = int(input())
a = int(input())
size = [input().rstrip() for _ in range(j)]
vis = [False]*j

for _ in range(a):
    s, n = input().split()
    n = int(n)
    if s == "L":
        if not vis[n-1] and size[n-1] in ("L"):
            vis[n-1] = True
    elif s == "M":
        if not vis[n-1] and size[n-1] in ("L", "M"):
            vis[n-1] = True
    else:
        if not vis[n-1] and size[n-1] in ("L", "M", "S"):
            vis[n-1] = True

print(sum(vis))
        