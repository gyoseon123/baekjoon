n = int(input())
dp = [[0]*20 for _ in range(n+1)]
dp[0][0] = 1
mod = int(1e9)

for i in range(1, n+1):
    exp = 0
    while 2**exp <= i:
        for j in range(exp+1):
            dp[i][exp] += dp[i-2**exp][j]%mod
        exp += 1

print(sum(dp[n])%mod)