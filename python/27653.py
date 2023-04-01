# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [0] + list(map(int, input().split()))
# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# ans = 0
# visited = [False]*(n+1)
# def dfs(node):
#     global ans
#     visited[node] = True
#     for next in graph[node]:
#         if not visited[next]:
#             ans += max(0, arr[next] - arr[node])
#             dfs(next)

# dfs(1)
# print(ans + arr[1])

import sys
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split()))
ans = sum(w)
for _ in range(n-1):
    a,b = map(int, input().split())
    ans -= min(w[a], w[b])
print(ans)