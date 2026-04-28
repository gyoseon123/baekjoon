import sys
input = sys.stdin.readline

def check(x):
    cnt = 1
    sm = 0
    for i in range(n):
        if sm + a[i] > x:
            cnt += 1
            sm = 0
        sm += a[i]
    return cnt <= m

n,m = map(int, input().split())
a = list(map(int, input().split()))

left = max(a)-1
right = int(1e18)
while left + 1 < right:
    mid = (left+right)//2
    
    if check(mid): right = mid
    else: left = mid

print(right)