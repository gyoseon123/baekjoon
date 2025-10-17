import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    
    if rank[a] < rank[b]: a,b = b,a
    
    parent[b] = a
    if (rank[a] == rank[b]): rank[a] += 1

n = int(input())
a = list(map(int, input().split()))
parent = [i for i in range(n+1)]
rank = [0]*(n+1)
indegree = [0]*(n+1)

for i in range(1, n+1):
    indegree[a[i-1]] += 1
    union(a[i-1], i)

ans = 0
s = set()
is_leaf = [0]*(n+1)

for i in range(1, n+1):
    if indegree[i] == 0:
        ans += 1
        is_leaf[find(i)] = 1
    s.add(find(i))

if len(s) > 1:
    ans += len(s)
    for i in list(s):
        if is_leaf[i]: ans -= 1

print(ans)