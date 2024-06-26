import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
path = []
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        path.append((graph[i][j],i,j))

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

ans = []

for c,a,b in path:
    if find(a) != find(b):
        if a == 1 and b == 2:
            print(find(a), find(b))
        union(a,b)
        ans.append((a+1,b+1))

for i in ans:
    print(*i)

    