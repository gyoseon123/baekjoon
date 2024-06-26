import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)] + [0]*100001
dp = [0]*10001
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
for i in range(2,n):
    dp[i] = max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i]
    dp[i] = max(dp[i-1], dp[i])
print(dp[n-1])
