import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
sl = sum(l)
tc = l.count(2)
n -= tc
while l.count(2) != 0:
    l.remove(2)
ssl = sum(l)
if sl%2 != 0:
    print("NO")
    exit()
    
w = sl//2

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        if j-l[i-1]  >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i-1]]+l[i-1])
        else:
            dp[i][j] = dp[i-1][j]


if n == 1: print("YES" if l[0] == 2 else "NO")
else:
    if dp[n][w] + tc >= w:
        print("YES")
    else:
        if dp[n][w] == w:
            if ssl%2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")