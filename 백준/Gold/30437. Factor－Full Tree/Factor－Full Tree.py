import sys
input = sys.stdin.readline

def pl(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False
    
    return [i for i in range(n+1) if prime[i]]

def find_dep(now):
    if ans[now] != -1:
        return 1
    return find_dep(parent[now]) + 1

def dfs(now, p):
    if ans[now] != -1:
        return ans[now]
    else:
        ans[now] = dfs(parent[now], p) * p
        return ans[now]

def dfs1(now):
    visited[now] = True
    
    for next in graph[now]:
        if not visited[next]:
            parent[next] = now
            dfs1(next)

n = int(input())
prime = pl(int(1e3))

ans = [-1]*(n+1)
ans[1] = 1

graph = [[] for _ in range(n+1)]
parent = [-1]*(n+1)
visited = [False]*(n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs1(1)

leaf = []

for i in range(1, n+1):
    if len(graph[i]) == 1 and parent[i] == graph[i][0]:
        leaf.append(i)
        
i = 0

while True:
    d = []
    for node in leaf:
        d.append((find_dep(node), node))
        
    if not d:
        break

    d.sort(reverse=True)
    dfs(d[0][1], prime[i])
    leaf.remove(d[0][1])
    i += 1

print(*ans[1:])