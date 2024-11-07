import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

dp = [[-int(1e9)]*2 for _ in range(n)]

dp[0][0] = l[0]

for i in range(1, n):
    dp[i][0] = max(l[i], dp[i-1][0] + l[i])
    dp[i][1] = max(dp[i-1][1] + l[i], dp[i-1][0])

print(max(map(max, dp)))