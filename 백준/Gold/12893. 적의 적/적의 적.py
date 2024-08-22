import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(now, color):
    ret = True
    visited[now] = color
    for next in graph[now]:
        if visited[next] == -1:
            ret = ret & dfs(next, (color+1)%2)
        else:
            if visited[next] == visited[now]:
                return False
    
    return ret

v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [-1]*(v+1)

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
res = []
for i in range(1, v+1):
    if visited[i] == -1:
        res.append(dfs(i, 0))
        
print(1 if all(res) else 0)