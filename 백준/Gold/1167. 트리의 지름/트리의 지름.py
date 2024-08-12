import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

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


n = int(input())
graph = [[] for _ in range(n+1)]

ans = 0
visited = [False]*(n+1)

for _ in range(n):
    l = list(map(int, input().split()))
    for j in range(1, len(l), 2):
        if l[j] == -1:
            break
        graph[l[0]].append((l[j], l[j+1]))
        graph[l[j]].append((l[0], l[j+1]))

dfs(1, 0)
print(ans)