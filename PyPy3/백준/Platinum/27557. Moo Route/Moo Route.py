import sys
input = sys.stdin.readline

mod = int(1e9) + 7

fac = [0]*1010101
fac[0] = 1
for i in range(1, 1010101):
    fac[i] = (fac[i-1] * i)%mod

inv_fac = [0]*1010101
inv_fac[1000000] = pow(fac[1000000], mod-2, mod)
for i in range(999999, -1, -1):
    inv_fac[i] = (inv_fac[i+1] * (i+1))%mod
    
def comb(n, k):
    return (fac[n] * (inv_fac[k] * inv_fac[n-k])%mod)%mod

n = int(input())
a = list(map(int, input().split()))
b = [i//2 for i in a]

ans = 1
for i in range(n-1):
    if b[i] <= b[i+1]:
        ans *= comb(b[i+1]-1, b[i]-1)
    else:
        ans *= comb(b[i], b[i+1])
    ans %= mod

print(ans)