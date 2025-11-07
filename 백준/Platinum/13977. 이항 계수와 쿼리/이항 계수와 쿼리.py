import sys
input = sys.stdin.readline

MAX = 4000001
mod = int(1e9) + 7

fac = [0]*MAX
fac[0] = 1
for i in range(1, MAX):
    fac[i] = (fac[i-1] * i)%mod

inv_fac = [0]*MAX
inv_fac[MAX-1] = pow(fac[MAX-1], mod-2, mod)
for i in range(MAX-2, -1, -1):
    inv_fac[i] = (inv_fac[i+1] * (i+1))%mod

def comb(n,k):
    return (fac[n] * (inv_fac[k] * inv_fac[n-k])%mod)%mod

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    print(comb(n,k))