import sys
input = sys.stdin.readline
n = int(input())
r,g,b = [], [], []
for i in range(n):
    x,y,z = map(int, input().split())
    r.append(x)
    g.append(y)
    b.append(z)
INF = int(1e9)
dp = [[INF]*3 for _ in range(n)]
dp[0][0] = r[0]
dp[0][1] = g[0]
dp[0][2] = b[0]

for i in range(1,n):
    dp[i][0] = min(dp[i][0], dp[i-1][1] + r[i], dp[i-1][2] + r[i])
    dp[i][1] = min(dp[i][1], dp[i-1][0] + g[i], dp[i-1][2] + g[i])
    dp[i][2] = min(dp[i][2], dp[i-1][0] + b[i], dp[i-1][1] + b[i])

print(min(dp[n-1]))
