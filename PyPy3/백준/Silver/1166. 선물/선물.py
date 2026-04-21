import sys
input = sys.stdin.readline

def check(x):
    v = (l//x) * (w//x) * (h//x)
    return v >= n

n,l,w,h = map(int, input().split())
left = 0
right = int(1e10)

for _ in range(500):
    mid = (left + right)/2
    
    if check(mid): left = mid
    else: right = mid

print(right)