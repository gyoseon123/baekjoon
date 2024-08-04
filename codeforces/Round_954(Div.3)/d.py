import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().rstrip()

    if n <= 2:
        print(int(s))
        continue
    
    dp = [[0]*2 for _ in range(n)] #dp[i][1] 이미 2칸을 건너 뜀 dp[i][0]은 아닌상태
    dp[0][0] = int(s[0])
    dp[1][0] = min(int(s[0]) + int(s[1]), int(s[0]) * int(s[1]))
    dp[1][1] = int(s[0] + s[1])
    for i in range(2, n):
        dp[i][0] = min(dp[i-1][0] + int(s[i]), dp[i-1][0] * int(s[i]))
        dp[i][1] = min(dp[i-1][1] + int(s[i]), dp[i-1][1] * int(s[i]), dp[i-2][0] + int(s[i-1] + s[i]), dp[i-2][0] * int(s[i-1] + s[i]))
    
    print(dp[n-1][1])

    
        


