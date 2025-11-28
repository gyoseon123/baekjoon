import sys
input = sys.stdin.readline
inf = sys.maxsize

def div(x):
    ret = []
    for i in range(1, x+1):
        if x%i == 0: ret.append(i)
    
    return ret

s = input().rstrip()
n = len(s)

table = [[0]*n for _ in range(n)]
dp = [["z"*202]*n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        itv = j - i + 1
        now = s[i:j+1]
        cnt = 0
        for k in range(i, n, itv):
            if s[k:k+itv] == now: cnt += 1
            else: break
        table[i][j] = cnt

for i in range(n):
    dp[i][i] = s[i]

for itv in range(n):
    for i in range(n):
        j = i + itv
        if j >= n: continue
        
        for k in range(i, j):
            nxt = dp[i][k] + dp[k+1][j]
            if len(nxt) < len(dp[i][j]): dp[i][j] = nxt
        
        d = div(itv+1)
        for k in range(len(d)):
            now = d[k]
            tlb = table[i][i+now-1]
            if 2 <= tlb and now * min(tlb, (itv+1)//now, 9) >= itv+1:
                nxt = f"{min(tlb, (itv+1)//now, 9)}({dp[i][i+now-1]})"
                if len(nxt) < len(dp[i][j]): dp[i][j] = nxt

print(dp[0][n-1])