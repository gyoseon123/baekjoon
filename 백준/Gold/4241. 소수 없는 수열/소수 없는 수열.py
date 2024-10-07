import sys
input = sys.stdin.readline

def plist(n):
    p = [True]*(n+1)
    p[0],p[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if p[i]: 
            for j in range(i*2, n, i): p[j] = False
    
    return p

pl = plist(10000)

def dfs(cnt):
    global flg
    if flg:
        return
    
    if cnt == m-n+1:
        flg = True
        print(*arr, sep=",")
    
    for i in range(n, m+1):
        if i in arrs: continue
        
        flag = True
        now = 0
        for length in range(2, d+1):
            if cnt + 1 >= length:
                now += arr[cnt+1-length]
                if pl[now+i]:
                    flag = False
                    
        if flag:
            arr.append(i)
            arrs.add(i)
            dfs(cnt+1)
            arr.pop()
            arrs.remove(i)        
        

while True:
    n,m,d = map(int, input().split())
    if (n,m,d) == (0,0,0): break
    arr = []
    arrs = set()
    flg = False
    dfs(0)
    if not flg:
        print("No anti-prime sequence exists.")