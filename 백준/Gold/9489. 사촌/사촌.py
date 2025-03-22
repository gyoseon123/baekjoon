import sys
input = sys.stdin.readline

def dfs(now, pre, cnt):
    depth[cnt].append(now)
    for next in graph[now]:
        if next != pre:
            parent[next] = now
            dfs(next, now, cnt+1)


while True:
    n,k = map(int, input().split())
    if (n,k) == (0,0): break
    l = list(map(int, input().split()))

    graph = [[] for _ in range(max(l)+1)]
    p = -1
    pre = l[0]
    for i in range(1, n):
        if l[i] - pre != 1:
            p += 1
        pre = l[i]
        graph[l[p]].append(l[i])
    
    depth = [[] for _ in range(n+1)]
    parent = [0]*(max(l)+1)

    
    dfs(l[0], -1, 0)

    for i in range(len(depth)):
        if k in depth[i]:
            start = i
            break
    
    if i <= 1:
        print(0)
        continue
    
    ans = 0
    for node in depth[start]:
        if parent[node] != parent[k] and parent[parent[node]] == parent[parent[k]]:
            ans += 1
    print(ans) 