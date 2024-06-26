n,m = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
dp = [[-1]*501 for _ in range(10001)] #dp[i][j] i분에 j지침지수로 뛸수있는 최대거리

dp[0][0] = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j-1] + arr[i]
    for j in range(1,m+1):
        if i-j >= 0:
                dp[i][0] = max(dp[i][0], dp[i-j][j], dp[i-j][0])
         
print(*dp, sep='\n')
print(dp[n][0])