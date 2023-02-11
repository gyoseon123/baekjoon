import sys
input = sys.stdin.readline
n,a,l = map(int, input().split())
attack = []
INF = int(1e9)
dp = [[-INF]*(l+1) for _ in range(n+1)]
dp[0][l] = a
for _ in range(n):
    x,y = map(int, input().split())
    attack.append((x,y))

tracking = [[()]*(l+1) for _ in range(n+1)]

for i in range(n):
    x,y = attack[i]
    for j in range(l+1):
        if x == -1:
            if j > y and dp[i+1][j-y] < dp[i][j]:
                dp[i+1][j-y] = dp[i][j]
                tracking[i+1][j-y] = (i,j,False)
        elif y == -1:
            if dp[i+1][j] < max(0, dp[i][j]-x):
                dp[i+1][j] = max(0, dp[i][j]-x)
                tracking[i+1][j] = (i,j,True)
        else:
            if dp[i][j] >= 0 and dp[i+1][j] < dp[i][j] - x:
                dp[i+1][j] = dp[i][j]-x
                tracking[i+1][j] = (i,j,True)
            if j - y > 0 and dp[i+1][j-y] < dp[i][j]:
                dp[i+1][j-y] = dp[i][j]
                tracking[i+1][j-y] = (i,j,False)

for i in range(1,l+1):
    if dp[n][i] >= 0:
        s = ''
        x,y = n,i
        while tracking[x][y]:
            if tracking[x][y][2]:
                s += 'A'
            else:
                s += 'L'
            x,y = tracking[x][y][0], tracking[x][y][1]
        print('YES')
        print(s[::-1])
        break
else:
    print('NO')