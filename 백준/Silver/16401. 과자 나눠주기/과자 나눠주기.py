import sys
input = sys.stdin.readline

def check(x):
    ret = 0
    for i in range(m):
        ret += l[i]//x
    return ret >= n

n,m = map(int, input().split())
l = list(map(int, input().split()))

left = 0
right = int(1e20)

while left + 1 < right:
    mid = (left+right)//2
    
    if check(mid): left = mid
    else: right = mid

print(left)

