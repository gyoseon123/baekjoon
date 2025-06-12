import sys
input = sys.stdin.readline

dp = [[0]*65 for _ in range(10)]

for i in range(10):
    dp[i][1] = 1

for i in range(10):
    for j in range(2, 65):
        for k in range(i+1):
            dp[i][j] += dp[k][j-1]

t = int(input())

for _ in range(t):
    n = int(input())
    print(sum([dp[i][n] for i in range(10)]))