import sys
input = sys.stdin.readline

def find(num):
    left = 0
    right = int(1e9)
    
    while left + 1 < right:
        mid = (left+right)//2
        if ((n-1)//mid) < num: right = mid
        else: left = mid
    return right

n = int(input())

now = 0
ans = 0
nxt = find(n)
v = n

while v != 0:
    ans += v*(nxt - now)
    now = nxt
    v = (n-1)//nxt
    nxt = find(v)

print(ans)