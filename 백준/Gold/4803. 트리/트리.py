import sys
input = sys.stdin.readline

def dfs(now, pre):
    visited[now] = True
    ret = True
    
    for next in graph[now]:
        if next != pre:
            if visited[next]: ret = False
            else: ret &= dfs(next, now)
    
    return ret

t = 1
while True:
    n,m = map(int, input().split())
    if (n,m) == (0,0): break
    
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, -1): cnt += 1
    
    print(f"Case {t}: ", end='')
    print("No trees." if cnt == 0 else "There is one tree." if cnt == 1 else f"A forest of {cnt} trees.")
    t += 1