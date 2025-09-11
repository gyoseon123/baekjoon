import sys
input = sys.stdin.readline

def check(P, p):
    ret = [0]*n
    now = p[0] + P
    ret[0] = now
    for i in range(1, n):
        if now >= p[i]:
            now = p[i] + P
        else:   
            v = P - (p[i] - now)
            if v > 0: 
                now += v
            else: return ret
        ret[i] = now
    
    return ret

L, n = map(int, input().split())
p = list(map(int, input().split()))
pr = [L - i for i in p[::-1]]

left = 0
right = L

while left + 1 < right:
    mid = (left+right)//2
    
    l = check(mid, p)
    r = check(mid, pr)
    r.reverse()
    
    flg = 0
    for i in range(n-1):
        if l[i] + r[i+1] >= L:
            flg = 1
            break
    
    if flg: right = mid
    else: left = mid

print(right)