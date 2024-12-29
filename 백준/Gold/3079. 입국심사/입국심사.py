import sys
input = sys.stdin.readline

def check(x):
    ret = 0
    for i in range(n):
        ret += x//t[i]
    return ret >= m

n,m = map(int, input().split())
t = [int(input()) for _ in range(n)]

left = 0
right = int(1e30)

while left + 1 < right:
    mid = (left+right)//2
    
    if check(mid): right = mid
    else: left = mid

print(right)