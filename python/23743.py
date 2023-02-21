import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append((c,a,b))
t = list(map(int, input().split()))
for i in range(1,n+1):
    graph.append((t[i-1], 0, i))
graph.sort()
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

parent = [i for i in range(n+1)]
ans = 0
for c,a,b in graph:
    if find(a) != find(b):
        union(a,b)
        ans += c
print(ans)