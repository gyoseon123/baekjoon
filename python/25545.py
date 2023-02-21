import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
if n > m or n == 1:
    print('NO')
    exit()
for i in range(m):
    a,b,c = map(int, input().split())
    if a > b:
        a,b = b,a
    graph.append((c,a,b,i+1))
graph.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return 

    if a > b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n+1)]
visited = [False]*(m+1)
for i in range(m):
    c,a,b = graph[i][0], graph[i][1], graph[i][2]
    if find(a) != find(b):
        visited[i] = True
        union(a,b)
for i in range(m):
    if not visited[i]:
        edge = graph[i]
        break
parent = [i for i in range(n+1)]
result = []
result.append(edge[3])
union(edge[1], edge[2])
for i in range(m):
    c,a,b = graph[i][0], graph[i][1], graph[i][2]
    if find(a) != find(b):
        result.append(graph[i][3])
        union(a,b)
print('YES')
print(*result)