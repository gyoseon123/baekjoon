n,a,l = map(int, input().split())
INF = int(1e9)
dp = [[-INF]*(l+1) for _ in range(n+1)]
path = [[()]*(l+1) for _ in range(n+1)]
dp[0][l] = a

q = []
for i in range(n):
    x,y = map(int, input().split())
    q.append((x,y))
for i in range(n):
    for j in range(l+1):
        x,y = q[i]
        if x == -1:
            if j > y:
                dp[i+1][j-y] = dp[i][j]
                path[i+1][j-y] = (i,j,'L')
        elif y == -1:
            dp[i+1][j] = max(dp[i][j]-x, 0)
            path[i+1][j] = (i,j,'A')
        else:
            if dp[i][j] >= x:
                dp[i+1][j] = dp[i][j]-x
                path[i+1][j] = (i,j,'A')
            if j > y:
                dp[i+1][j-y] = dp[i][j]
                path[i+1][j-y] = (i,j,'L')
sig = False
for i in range(1,l+1):
    if dp[n][i] >= 0:
        result = ''
        while True:
            if path[n][i] == ():
                sig = True
                break
            x,y,s = path[n][i]
            result += s
            n,i = x,y
    if sig:
        break
else:
    print('NO')
if sig:
    print('YES')
    print(result[::-1])
            
