import sys
input = sys.stdin.readline
n = int(input())
Ai = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1,n+1):
    m = 0
    for j in range(i):
        if Ai[j] < Ai[i]:
            if dp[j] > m:
                m = dp[j]
    dp[i] = m+1
print(max(dp))
