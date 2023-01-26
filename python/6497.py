import sys
input = sys.stdin.readline
while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    path = []
    parent = [i for i in range(n+1)]
    w = 0
    for _ in range(m):
        l = list(map(int, input().split()))
        a,b,c = map(int, l)
        path.append((c,a,b))
        w += c
    path.sort()
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a,b):
        a = find(a)
        b = find(b)
        if a == b: return False
    
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    ans = 0
    for c,a,b in path:
        if find(a) != find(b):
            ans += c
            union(a,b)
    print(w - ans)
    