import sys
input = sys.stdin.readline
INF = sys.maxsize

def dfs(now, visit):
    if visit == (1 << n)-1:
        if graph[now][0] != 0:
            return graph[now][0]
        else:
            return INF

    if dp[now][visit] != -1:
        return dp[now][visit]
    
    ret = INF
    for i in range(1, n):
        if graph[now][i] != 0 and not visit & (1 << i):
            ret = min(ret, dfs(i, visit | (1 << i)) + graph[now][i])

    dp[now][visit] = ret
    return ret

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(1 << n) for _ in range(n)]

print(dfs(0, 1))