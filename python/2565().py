import sys
input = sys.stdin.readline
n = int(input())
Ai = [0] * 501
dp = [0] * 501
dp_2 = [0] * 501
for i in range(n):
    a,b = map(int, input().split())
    Ai[a] = b
for i in range(1,501):
    m = 0
    for j in range(i):
        if Ai[j] < Ai[i]:
            if dp[j] > m:
                m = dp[j]
    dp[i] = m+1

for i in range(1,501):
    m = 0
    for j in range(i):
        if Ai[j] > Ai[i]:
            if dp_2[j] > m:
                m = dp_2[j]
    dp_2[i] = m+1

print(dp)