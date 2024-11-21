import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(now):
    visited[now] = True
    ret = 1
    
    for next in graph[now]:
        if not visited[next]:
            ret += dfs(next)
    
    answer[now] = ret
    return ret
    

n,r,q = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = [0]*(n+1)
visited = [False]*(n+1)

for _ in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for _ in range(q):
    qry = int(input())
    print(answer[qry])