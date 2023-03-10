import sys
input = sys.stdin.readline
n,m = map(int, input().split())
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j,k in enumerate(list(map(int, input().split()))):
        dp[i+1][j+1] = k
for i in range(1,n+1):
    for j in range(1,n):
        dp[i][j+1] += dp[i][j]
for i in range(1,n):
    for j in range(1,n+1):
        dp[i+1][j] += dp[i][j]

for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])