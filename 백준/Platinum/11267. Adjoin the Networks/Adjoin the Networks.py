import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now, cost):
    global ans
    visited[now] = True
    ret = []
    for next, cst in graph[now]:
        if not visited[next]:
            d = dfs(next, cst)
            ret.append(d)
    
    if not ret:
        return cost
    
    ret.sort(reverse=True)
    if len(ret) == 1:
        ans = max(ans, ret[0])
    elif len(ret) >= 2:
        ans = max(ans, ret[0]+ret[1])
    return max(ret) + cost


c,l = map(int, input().split())
graph = [[] for _ in range(c)]

for _ in range(l):
    u,v = map(int, input().split())
    graph[u].append((v,1))
    graph[v].append((u,1))

visited = [False]*c
d = []

for i in range(c):
    ans = 0
    if not visited[i]:
        dfs(i, 0)
        d.append(ans)
        
d.sort(reverse=True)

if len(d) == 1:
    print(d[0])
elif len(d) == 2:
    print(max(d[0], (d[0]+1)//2 + (d[1]+1)//2 + 1))
else:
    print(max(d[0], (d[0]+1)//2 + (d[1]+1)//2 + 1, (d[1]+1)//2 + (d[2]+1)//2 + 2))

    