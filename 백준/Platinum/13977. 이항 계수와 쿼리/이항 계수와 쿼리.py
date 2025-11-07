import sys
input = sys.stdin.readline
mod = 1000000007


def power(n,cnt):
    if cnt == 1:
        return n
    
    div = power(n,cnt//2)
    if cnt&1:
        return (div*div*n)%mod
    else:
        return (div*div)%mod
    
fac = [0]*(4000000+1)
fac[0] = 1
x = 1
for i in range(1,4000000+1):
    x = (x*i)%mod
    fac[i] = x

m = int(input())
for _ in range(m):
    n,k = map(int, input().split())
    print((fac[n]*power((fac[n-k]*fac[k]),mod-2))%mod)
