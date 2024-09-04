import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    a = []
    
    for i in range(0, n*2, 2):
        a.append((l[i], l[i+1]))
        
    a.sort()
    vis = [False]*n
    
    ans = 0
    cnt = 0
    while True:
        if cnt == n: break
        
        flg = False
        now = 0
        for i in range(n):
            if vis[i]: continue
            
            if flg:
                if a[now][0] <= a[i][0] and a[now][1] <= a[i][1]:
                    now = i
                    vis[i] = True
                    cnt += 1
            else:
                ans += 1
                now = i
                vis[i] = True
                cnt += 1
                flg = True

    print(ans)