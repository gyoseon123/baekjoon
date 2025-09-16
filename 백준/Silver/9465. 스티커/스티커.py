import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(a[0][0], a[1][0]))
        continue
    elif n == 2:
        print(max(a[0][0] + a[1][1], a[0][1] + a[1][0]))
        continue
    
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]
    dp[0][1] = a[1][0] + a[0][1]
    dp[1][1] = a[0][0] + a[1][1]
    
    for i in range(2, n):
        dp[0][i] = max(dp[0][i-2], dp[1][i-2], dp[1][i-1]) + a[0][i]
        dp[1][i] = max(dp[0][i-2], dp[1][i-2], dp[0][i-1]) + a[1][i]
    
    print(max(map(max, dp)))