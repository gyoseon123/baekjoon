import sys
input = sys.stdin.readline

def check(x):
    ret = 0
    now = 0
    for i in range(n):
        if l[i] > now:
            now = x
            ret += 1
            if now < l[i]: return False
            now -= l[i]
        else:
            now -= l[i]
    
    return ret <= m
        


n,m = map(int, input().split())
l = [int(input()) for _ in range(n)]

left = 0
right = int(1e9)

while left + 1 < right:
    mid = (left + right)//2

    if check(mid):
        right = mid
    else:
        left = mid

print(right)