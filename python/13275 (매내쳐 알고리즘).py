import sys
input = sys.stdin.readline
s = "#"+"#".join(input())+"#"

n = len(s)
dp = [0]*n
p,r = -1,-1
for i in range(n):
    if i > r:
        p = i
        r = i
        while (r < n and r <= 2*p and s[r] == s[2*p-r]): r += 1
        r -= 1
        dp[i] = r-p
    else:
        j = 2*p - i
        if dp[j] < r-i:
            dp[i] = dp[j]
        elif dp[j] > r-i:
            dp[i] = r-i
        else:
            p = i
            while (r < n and r <= 2*p and s[r] == s[2*p-r]): r += 1
            r -= 1
            dp[i] = r-p

print(max(dp))


