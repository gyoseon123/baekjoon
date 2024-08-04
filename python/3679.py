import math

def dist(x1,y1,x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

c = int(input())
for _ in range(c):
    n,*l = map(int, input().split())
    point = []
    for i in range(n):
        point.append((l[i*2], l[i*2+1], i))
    
    center = (sum([i[0] for i in point])/n, sum([i[1] for i in point])/n)

    point.sort(key= lambda x : (math.atan2(x[1] - center[1], x[0] - center[0]), dist(*center, *x[:2])))
    print(*[i[2] for i in point])