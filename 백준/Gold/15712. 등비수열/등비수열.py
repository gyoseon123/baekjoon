def solve(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return (solve(n//2)*(1 + pow(r, n//2, mod)))%mod
    else:
        return (solve(n-1) + pow(r, n-1, mod))%mod

a,r,n,mod = map(int, input().split())
print(a*solve(n)%mod)