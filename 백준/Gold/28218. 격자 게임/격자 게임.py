import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dp = [[-1]*(m+1) for _ in range(n+1)]
dp[n][m] = 0

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if dp[i][j] == -1 and board[i-1][j-1] != "#":
            arr = []
            if i + 1 <= n and dp[i+1][j] != -1:
                arr.append(dp[i+1][j])
            if j + 1 <= m and dp[i][j+1] != -1:
                arr.append(dp[i][j+1])
            
            for kk in range(1, k+1):
                if 0 <= i + kk <= n and 0 <= j + kk <= m and dp[i+kk][j+kk] != -1:
                    arr.append(dp[i+kk][j+kk])
            
            if all(arr):
                dp[i][j] = 0
            else:
                dp[i][j] = 1

q = int(input())
for _ in range(q):
    x,y = map(int, input().split())
    print("First" if dp[x][y] == 1 else "Second")