import sys
input = sys.stdin.readline
n,k = map(int, input().split())
W = []
V = []
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    w,v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1,n+1):
    for j in range(1,k+1):
        if j-W[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]]+V[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])