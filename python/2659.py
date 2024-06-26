import sys
sys.setrecursionlimit
n = int(input())
l = [[0]*n for _ in range(n)]
l[0][0] = 1
def dfs(pos,a,b):
    if l[a][b] == n*(n+1)//2:
        return 
    
    if pos == 1: # 아래 
        if a+1 >= n or l[a+1][b] != 0:
            dfs(2,a,b)
            return 
        l[a+1][b] = l[a][b] + 1
        dfs(pos,a+1,b)
    if pos == 2: # 오르쪽
        if b+1 >= n or l[a][b+1] != 0:
            dfs(3,a,b)
            return
        l[a][b+1] = l[a][b] + 1
        dfs(pos,a,b+1)
    if pos == 3:
        if l[a-1][b-1] != 0:
            dfs(1,a,b)
            return
        l[a-1][b-1] = l[a][b] +1
        dfs(pos,a-1,b-1)

dfs(1,0,0)

for i in range(n):
    for j in range(n):
        if l[i][j] != 0:
            pass
   