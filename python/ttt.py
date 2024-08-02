import sys
input = sys.stdin.readline

def check(h):
    if n == 1:
        return 0
    
    ret = 0
    for i in range(n):
        if i == 0:
            if abs(l[1] - l[0]) > h:
                ret += 1
        elif i == n-1:
            if abs(l[n-1] - l[n-2]) > h:
                ret += 1
        else:
            if abs(l[i] - l[i-1]) > h or abs(l[i+1] - l[i]) > h:
                ret += 1
    
    return ret



n,k = map(int, input().split())
l = list(map(int, input().split()))

left = -1
right = int(1e9)+7

while left + 1 < right:
    mid = (left+right)//2

    if check(mid) <= k:
        right = mid
    else:
        left = mid

print(right)


