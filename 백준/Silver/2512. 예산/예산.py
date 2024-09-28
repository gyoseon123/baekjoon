import sys
input = sys.stdin.readline

def f(x):
    ret = 0
    for i in range(n):
        ret += min(l[i], x)
    return ret

n = int(input())
l = list(map(int, input().split()))
m = int(input())

left = 0
right = max(l)+1

while left + 1 < right:
    mid = (left+right)//2
    
    if f(mid) <= m:
        left = mid
    else:
        right = mid

print(left)