import sys
input = sys.stdin.readline

def solve(left, right):
    if left == right:
        return h[left]
    
    mid = (left+right)//2
    ret = max(solve(left, mid), solve(mid+1, right))
    lo = mid 
    hi = mid+1
    height = min(h[lo], h[hi])
    while left < lo or hi < right:
        if hi < right and (lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])
        ret = max(ret, height*(hi-lo+1))
    ret = max(ret, height*2)

    return ret

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    n,*h = arr
    print(solve(0,n-1))
