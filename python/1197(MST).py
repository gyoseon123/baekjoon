import sys
input = sys.stdin.readline
v,e = map(int, input().split())
path = []
parent = [i for i in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    path.append((c,a,b))
path.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for c,a,b in path:
    if find(a) != find(b):
        ans += c
        union(a,b)

print(ans)