def solve(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return (solve(n//2)*(1 + pow(a, n//2, m)))%m
    else:
        return (solve(n-1) + pow(a, n-1, m))%m

m,a,c,X0,n,g = map(int, input().split())

if a == 1:
    print(int(((X0 + c*n)%m)%g))
else:
    print(((X0*pow(a, n, m) + c*solve(n))%m)%g)