import math

def cal_dis(x1,y1,x2,y2):
    return math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))

def find_circle_mid(x1,y1,x2,y2):
    d = cal_dis(x1, y1, x2, y2)
    if d > 2:
        return False

    c1 = ((x1+x2)/2 + math.sqrt(1 - (d/2)**2)*((y2 - y1)/d), (y1+y2)/2 - math.sqrt(1 - (d/2)**2)*((x2 - x1)/d))
    c2 = ((x1+x2)/2 - math.sqrt(1 - (d/2)**2)*((y2 - y1)/d), (y1+y2)/2 + math.sqrt(1 - (d/2)**2)*((x2 - x1)/d))
    return [c1, c2]

def cnt_cir(rx, ry):
    ret = 0
    for x,y in point:
        if cal_dis(x,y,rx,ry) <= 1 + 1e-9:
            ret += 1
    return ret

while True:
    n = int(input())
    if n == 0:
        break

    ans = 1
    point = [list(map(float, input().split())) for _ in range(n)]

    if n == 1:
        print(1)
        continue

    for i in range(n):
        for j in range(i+1, n):
            p1 = point[i]
            p2 = point[j]
            f = find_circle_mid(*p1, *p2)
            if f != False:
                ans = max(ans, cnt_cir(*f[0]), cnt_cir(*f[1]))

    print(ans)