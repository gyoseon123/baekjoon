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
    if rank[a] == rank[b]:
        rank[b] += 1
        
def dfs(now, max_v, target_node):
    global ret
    
    if now == target_node:
        ret = max_v
        return
    
    visited[now] = True
    
    for next, cost in mst_graph[now]:
        if not visited[next]:
            dfs(next, max(max_v, cost), target_node)
        
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
rank = [0]*(n+1)
edges = []

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    edges.append((c,a,b))

edges.sort()
use_edges = set()
mst_graph = [[] for _ in range(n+1)]

mst_val = 0
for c,a,b in edges:
    if find(a) != find(b):
        mst_graph[a].append((b,c))
        mst_graph[b].append((a,c))
        union(a,b)
        mst_val += c

q = int(input())

for _ in range(q):
    a,b = map(int, input().split())
    visited = [False]*(n+1)
    ret = 0
    dfs(a, -1, b)
    print(mst_val - ret)