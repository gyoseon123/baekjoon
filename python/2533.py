import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(now):
    visited[now] = True

    dp[now][1] = 1

    for next in graph[now]:
        if not visited[next]:
            dfs(next)
            dp[now][0] += dp[next][1]
            dp[now][1] += min(dp[next][0], dp[next][1])

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dp = [[0]*2 for _ in range(n+1)] #dp[i][1] = i노드가 얼리어답터일때 최솟값
ans = 0

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(min(dp[1][0], dp[1][1]))
