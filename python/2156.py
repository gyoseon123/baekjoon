import sys
input = sys.stdin.readline
n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0]*n
dp[0] = wine[0]
dp[1] = wine[1]