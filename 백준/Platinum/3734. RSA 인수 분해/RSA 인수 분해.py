import math
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

m = math.isqrt(n//k + (10**10) // (4*k*k))

for i in range(max(2, m - int(1e5)//(2*k)), m + int(1e5)//(2*k)+1):
    if n%i == 0:
        p,q = min(i, n//i), max(i, n//i)
        break

print(f"{p} * {q}")