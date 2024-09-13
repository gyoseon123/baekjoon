import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now, parent):
    global cnt
    cnt += 1
    visited[now] = cnt
    ret = visited[now]
    
    for next in graph[now]:
        if next == parent: continue
        
        if not visited[next]:
            low = dfs(next, now)
            ret = min(ret, low)
            
            if low > visited[now]:
                res.append((min(now, next), max(now, next)))
        else:
            ret = min(ret, visited[next])
    
    return ret
    


v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(v+1)
res = []

dfs(1, 0)

res.sort()

print(len(res))
for a,b in res:
    print(a,b)