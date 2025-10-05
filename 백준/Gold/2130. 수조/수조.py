import sys
input = sys.stdin.readline

def check(x):
    ret = 0
    for i in range(n):
        b, h, w, d = tank[i]
        if b >= x: continue
        ret += (min(b + h, x) - b) * w * d
    return ret < v

n = int(input())
tank = [list(map(int, input().split())) for _ in range(n)]
v = int(input())

vol = 0
for i in range(n):
    vol += tank[i][1] * tank[i][2] * tank[i][3]
    
if vol < v:
    print("OVERFLOW")
    exit()

left = 0
right = 1e9

for _ in range(100):
    mid = (left+right)/2
    
    if check(mid): left = mid
    else: right = mid

print(f"{right:.2f}")