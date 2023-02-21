import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0]*(n+1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return


    if rank[a] > rank[b]:
        a,b = b,a
    
    parent[a] = b
    if rank[a] == rank[b]:
        rank[b] += 1
   
for i in range(m):
    q,a,b = map(int, input().split())
    if q == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')