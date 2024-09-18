n = int(input())
k = int(input())

def check(num):
    ret = 0
    for i in range(1,n+1):
        ret += min(n, num//i)
    return ret >= k

lo = 0
hi = n*n+1
while lo + 1 < hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)
