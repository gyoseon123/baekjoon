from itertools import permutations

s2 = 2**0.5
dx = [0,1,s2,1,0,-1,-s2,-1]
dy = [s2,1,0,-1,-s2,-1,0,1]

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def trans(arr):
    ret = []
    for i in range(8):
        ret.append((arr[i]*dx[i], arr[i]*dy[i]))
    return ret

def is_able(points):
    for i in range(8):
        if ccw(*points[i], *points[(i+1)%8], *points[(i+2)%8]) > 0:
            return False
    return True

l = list(map(int, input().split()))
ans = 0

for p in permutations(l, 8):
    tl = trans(p)
    if is_able(tl):
        ans += 1
        
print(ans)