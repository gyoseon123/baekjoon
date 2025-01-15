import sys
input = sys.stdin.readline

def check(x):
    ret = 0
    
    for i in range(n):
        ret += max(0, A[i] - x)
    
    return ret >= m

n,m = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = int(2e9)

while left + 1 < right:
    mid = (left+right)//2
    
    if check(mid): left = mid
    else: right = mid

print(left)