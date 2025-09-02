import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = [0]*(n-1)
left = [0]*n
right = [0]*n

for i in range(n-1):
    b[i] = a[i+1] - a[i]

for i in range(1, n):
    left[i] = left[i-1] + max(0, 1 - b[i-1])

for i in range(n-2, -1, -1):
    right[i] = right[i+1] + max(0, 1 + b[i])

ans = int(1e18)

for i in range(n):
    ans = min(ans, max(left[i], right[i]))

print(ans)