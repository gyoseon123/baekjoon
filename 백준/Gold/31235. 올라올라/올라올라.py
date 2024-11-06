import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

res = 0
now = 0
max_v = -1
for i in range(n):
    if max_v <= a[i]:
        max_v = a[i]
        now = 0
    else:
        now += 1
    res = max(res, now)
    
print(res+1)