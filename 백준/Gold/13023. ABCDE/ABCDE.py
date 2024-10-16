import sys
input = sys.stdin.readline
sys.setrecursionlimit(202020)

def dfs(now, dep):
    global flg
    if dep >= 4:
        flg = True
        return
    
    for next in graph[now]:
        if not visit[next]:
            visit[next] = True
            dfs(next, dep+1)
            visit[next] = False

n,m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False]*n
flg = False

for i in range(n):
    visit[i] = True
    dfs(i, 0)
    visit[i] = False
    if flg: break
    
print(1 if flg else 0)