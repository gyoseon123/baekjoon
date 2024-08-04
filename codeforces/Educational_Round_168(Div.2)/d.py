import sys
input = sys.stdin.readline

def dfs(now, val):
    visited[now] = True

    ret = int(1e12)
    for next in graph[now]:
        if not visited[next]:
            ret = min(ret, dfs(next, a[next-1]))
    
    if now == 1:
        if ret == int(1e12):
            return val
        else:
            return val + ret

    if ret == int(1e12):
        return val
    

    if ret > val:
        return val + (ret - val)//2
    else:
        return ret
    

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n+10)]
    p = list(map(int, input().split()))
    for i in range(n-1):
        graph[p[i]].append(i+2)
        graph[i+2].append(p[i])
    

    visited = [False]*(n+10)
    print(dfs(1, a[0]))
