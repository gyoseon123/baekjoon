n,k = map(int, input().split())
mod = 1000000007

def fac(n):
    result = 1
    for i in range(2,n+1):
        result = (result*i)%mod
    return result

def power(n,cnt):
    if cnt == 1:
        return n
    
    div = power(n,cnt//2)
    if cnt&1:
        return (div*div*n)%mod
    else:
        return (div*div)%mod

print((fac(n)*power((fac(n-k)*fac(k)),mod-2))%mod)

