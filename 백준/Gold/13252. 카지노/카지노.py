def f(now, cnt):
    if cnt == k:
        if now >= 1:
            return 1
        else: return 0
    
    if now == 0: return 0
    
    try: 
        if dp[(now, cnt)]:
            return dp[(now, cnt)]
    except:
        pass
    
    dp[(now, cnt)] =  f(now - now//m, cnt+1)*((m - now%m)/m) + f(now - now//m-1, cnt+1)*((now%m)/m)
    return dp[(now, cnt)]
        
dp = {}

n,m,k = map(int, input().split())
print(f(n, 0))
