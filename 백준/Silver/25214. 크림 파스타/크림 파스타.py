import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

d = l[0]
ans = 0
print(0, end=' ')

for i in range(1, n):
    d = min(d, l[i])
    if l[i] - d > ans:
        ans = l[i] - d
    print(ans, end=' ')
