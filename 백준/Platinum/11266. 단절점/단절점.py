import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now, is_root):
    global cnt
    cnt += 1
    visited[now] = cnt
    ret = visited[now]
    child = 0
    
    for next in graph[now]:
        if not visited[next]:
            child += 1
            low = dfs(next, False)
            ret = min(ret, low)
            
            if not is_root and low >= visited[now]:
                cut_vertex[now] = True
        else:
            ret = min(ret, visited[next])
    
    if is_root and child >= 2:
        cut_vertex[now] = True
    
    return ret
    


v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(v+1)
cut_vertex = [False]*(v+1)

for i in range(1, v+1):
    if not visited[i]:
        dfs(i, True)

res = []
for i in range(1, v+1):
    if cut_vertex[i]:
        res.append(i)

print(len(res))
print(*res)