import sys
input = sys.stdin.readline
n,m = map(int, input().split())
path = []
parent = [i for i in range(n+1)]
for i in range(m):
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

    if a == b:
        return 

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
ans = 0
cnt = 0
for c,a,b in path:
    if find(a) != find(b) and cnt < n-2:
        union(a,b)
        ans += c
        cnt += 1
print(ans)