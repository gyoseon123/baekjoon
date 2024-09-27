import sys
input = sys.stdin.readline

def check(w):
    cnt = 0
    ret = 0
    for i in range(n):
        if l[i] >= w:
            cnt += 1
        else:
            cnt = 0
        ret = max(ret, cnt)
        
    return ret >= w

n = int(input())
l = list(map(int, input().split()))

left = 0
right = n+1

while left + 1 < right:
    mid = (left+right)//2
    
    if check(mid):
        left = mid
    else:
        right = mid

print(left)