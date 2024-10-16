import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a == b: return
    
    if rank[a] < rank[b]:
        a,b = b,a
    
    parent[a] = b
    set_size[b] += set_size[a]
    if rank[a] == rank[b]:
        rank[b] += 1


n,m,q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
query = [int(input()) for _ in range(q)]
parent = [i for i in range(n+1)]
rank = [0]*(n+1)
set_size = [1]*(n+1)

qs = set(query)

for i in range(1, m+1):
    if i not in qs:
        a,b = edges[i-1]
        union(a,b)
        
query.reverse()
ans = 0

for i in range(q):
    a,b = edges[query[i]-1]
    if find(a) != find(b):
        ans += set_size[find(a)]*set_size[find(b)]
        union(a,b)        

print(ans)