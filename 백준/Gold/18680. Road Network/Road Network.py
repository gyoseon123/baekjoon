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

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        x,y = map(int, input().split())
        graph[x].append((y, 1))
        graph[y].append((x, 1))
    
    visited = [False]*(n+1)
    ans = 0
    dfs(1, 0)
    print(n - ans - 1)