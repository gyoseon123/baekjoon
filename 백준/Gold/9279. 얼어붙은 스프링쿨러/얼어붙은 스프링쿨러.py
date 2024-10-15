import sys
input = sys.stdin.readline
INF = sys.maxsize

def dfs(now, parent, cost):
    ret = 0
    
    for next, cst in graph[now]:
        if next != parent:
           ret += dfs(next, now, cst)
    
    return cost if not ret or cost < ret else ret 
    
while True:
    try: n,c = map(int, input().split())
    except: break
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    print(dfs(c, -1, INF))
    