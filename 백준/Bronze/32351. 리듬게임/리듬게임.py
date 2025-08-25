import sys
input = sys.stdin.readline

n, s0, k = input().split()
n = int(n)
s0 = float(s0)
k = int(k)

now = 1
b = s0
ans = 0

for _ in range(k):
    mi, si = input().split()
    mi = int(mi)
    si = float(si)
    ans += (mi - now) * (240 / b)
    now = mi
    b = si

ans += (n - now + 1) * (240 / b)

print(f"{ans:.12f}")