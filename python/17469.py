import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if rank[a] > rank[b]:
        a,b = b,a
    
    parent[a] = b
    color[b] |= color[a]

    if rank[a] == rank[b]:
        rank[b] += 1

n,q = map(int, input().split())
edge = []
query = []
parent = [i for i in range(n+1)]
rank = [0]*(n+1)
color = [set()]*(n+1)

for _ in range(n-1):
    edge.append(int(input()))

for i in range(1,n+1):
    c = int(input())
    color[i].add(c)
    
for _ in range(n+q-1):
    query.append(list(map(int, input().split())))

for i in range(n+q-2, -1, -1):
    qry = query[i]
    if qry[0] == 1:
        union(qry[1], edge[qry[1]-2])
    else:
        print(len(color[find(qry[1])]))
print(color)