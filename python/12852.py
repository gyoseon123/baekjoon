import sys
input = sys.stdin.readline
x = int(input())
dp = [0] * 1000001

for i in range(2,1000001):
    if i%3 == 0 and i%2 == 0:
        dp[i] = min(dp[i-1], dp[i//3], dp[i//2])+1
    elif i%3 == 0:
        dp[i] = min(dp[i-1], dp[i//3])+1
    elif i%2 == 0:
        dp[i] = min(dp[i-1], dp[i//2])+1
    else:
        dp[i] = dp[i-1]+1
result = []
print(dp[x])
while True:
    result.append(x)
    if x == 1:
        break
    if x%3 == 0 and x%2 == 0:
        m = min(dp[x//3], dp[x//2], dp[x-1])
        if dp[x//3] == m:
            x = x//3
        elif dp[x//2] == m:
            x = x//2
        else:
            x = x-1
    elif x%2 == 0:
        if dp[x//2] <= dp[x-1]:
            x = x//2
        else:
            x = x-1
    elif x%3 == 0:
        if dp[x//3] <= dp[x-1]:
            x = x//3
        else:
            x = x-1
    else:
        x = x-1

print(*result)
