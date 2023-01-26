import sys
input = sys.stdin.readline
n,k = map(int, input().split())
coin = []
INF = int(1e9)
dp = [INF]*(k+1)
dp[0] = 0
for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(i,k+1):
        dp[j] = min(dp[j-i]+1, dp[j])

if dp[k] != INF:
    print(dp[k])
else:
    print(-1)


