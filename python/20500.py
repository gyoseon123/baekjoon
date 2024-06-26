n = int(input())
dp = [0,1,1]
MOD = 1000000007
for i in range(1515):
    dp.append((dp[-2]*2 + dp[-1])%MOD)
print(dp[n-1])