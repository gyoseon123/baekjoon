import bisect
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now):
    if res[now] != -1: return res[now]
    
    if not idx[l[now][1]]:
        res[now] = l[now][1]
        return res[now]
    
    next_idx = bisect.bisect_left(idx[l[now][1]], now+1)
    if next_idx >= len(idx[l[now][1]]):
        res[now] = l[now][1]
        return res[now]
    
    next = idx[l[now][1]][next_idx]
    if next <= now:
        res[now] = l[now][1]
        return res[now]
    
    res[now] = dfs(next)
    return res[now]
    
n,m = map(int, input().split())

fir_idx = [-1]*(n+1)
res = [-1]*(m+1)
l = []

for i in range(m):
    u,v = map(int, input().split())
    l.append((u,v))
    if fir_idx[u] == -1: fir_idx[u] = i
    
idx = [[] for _ in range(n+1)]

for i in range(m):
    idx[l[i][0]].append(i)

# print(fir_idx)
for i in range(1, n+1):
    if fir_idx[i] == -1:
        print(i, end=' ')
    else:
        print(dfs(fir_idx[i]), end=' ')
