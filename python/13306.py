import sys
input = sys.stdin.readline

n,q = map(int, input().split())
edge = []
for _ in range(n-1):
    edge.append(int(input()))
query = []
for _ in range(n+q-1):
    l = list(map(int, input().split()))
    query.append(l)

parent = [i for i in range(n+1)]
rank = [0] * (n+1)
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
    
    if rank[a] == rank[b]:
        rank[b] += 1

query.reverse()
answer = []
for qry in query:
    if len(qry) == 2:
        union(qry[1], edge[qry[1]-2])
    else:
        if find(qry[1]) == find(qry[2]):
            answer.append(True)
        else:
            answer.append(False)

answer.reverse()
for i in answer:
    if i:
        print('YES')
    else:
        print('NO')
