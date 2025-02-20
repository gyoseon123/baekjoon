import sys
input = sys.stdin.readline

def solve(n,m,coins):
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i],m+1):
            dp[j] += dp[j-coins[i]]
    print(dp[m])

t = int(input())
for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    solve(n,m,coins)