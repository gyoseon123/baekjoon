import sys
input = sys.stdin.readline

def gcd(a,b):
    if b != 0:
        return gcd(b, a%b)
    return a

def find_area(points):
    numX = []
    numY = []
    sumP, sumM = 0, 0
    for x,y in points:
        numX.append(x)
        numY.append(y)
    numX.append(numX[0])
    numY.append(numY[0])
    for i in range(len(points)):
        sumP += numX[i]*numY[i+1]
        sumM += numX[-i-1]*numY[-i-2]
        
    return abs(sumP - sumM)//2

def cnt(px1, py1, px2, py2):
    dx = abs(px1 - px2)
    dy = abs(py1 - py2)
    return gcd(dx, dy) + 1

def ccw(x1, y1, x2, y2, x3, y3):
    return (x3 - x1)*(y2 - y1) - (y3 - y1)*(x2 - x1)

def convex_hull(points):
    points.sort()
    
    stk1 = []
    stk2 = []
    
    for point in points:
        while len(stk1) >= 2 and ccw(*stk1[-2], *stk1[-1], *point) >= 0: stk1.pop()
        while len(stk2) >= 2 and ccw(*stk2[-2], *stk2[-1], *point) <= 0: stk2.pop()
        
        stk1.append(point)
        stk2.append(point)
    
    return stk1 + list(reversed(stk2[1:len(stk2)-1]))

def convex_hull2(points):
    points.sort()
    
    stk1 = []
    stk2 = []
    
    for point in points:
        while len(stk1) >= 2 and ccw(*stk1[-2], *stk1[-1], *point) >= 0: stk1.pop()
        while len(stk2) >= 2 and ccw(*stk2[-2], *stk2[-1], *point) <= 0: stk2.pop()
        
        stk1.append(point)
        stk2.append(point)
    
    return (stk2, stk1)

def find_line(x1, y1, x2, y2):
    if x1 - x2 == 0:
        return (1, 0, -x1)
    d = (y1 - y2)/(x1 - x2)
    return (d, -1, -d*x1 + y1)

def cnt(px1, py1, px2, py2):
    dx = abs(px1 - px2)
    dy = abs(py1 - py2)
    return gcd(dx, dy) + 1

def is_in(point):
    if point[0] < up[0][0] or point[0] > up[-1][0]:
        return False
    
    
    left = 0
    right = len(up)
    
    while left + 1 < right:
        mid = (left + right)//2
        
        if up[mid][0] <= point[0]:
            left = mid
        else:
            right = mid
    
    if left == len(up)-1:
        ret1 = left-1
    else:
        ret1 = left
    
    left = 0
    right = len(down)
    
    while left + 1 < right:
        mid = (left + right)//2
        
        if down[mid][0] <= point[0]:
            left = mid
        else:
            right = mid
    
    if left == len(down)-1:
        ret2 = left-1
    else:
        ret2 = left
    
    upline = find_line(*up[ret1], *up[ret1+1])
    downline = find_line(*down[ret2], *down[ret2+1])
    if upline[1] == 0:
        if up[ret1][1] <= point[1] <= up[ret1+1][1]:
            return True
        else:
            return False
    upy = (-upline[0]*point[0] - upline[2])/upline[1]
    if downline[1] == 0:
        if down[ret2][1] <= point[1] <= down[ret2+1][1]:
            return True
        else:
            return False
    
    downy = (-downline[0]*point[0] - downline[2])/downline[1]
    
    if downy <= point[1] <= upy:
        return True
    else:
        return False

n,m = map(int, input().split())

boom = [tuple(map(int, input().split())) for _ in range(n)]
protect = [tuple(map(int, input().split())) for _ in range(m)]

if n == 1:
    if boom[0] in protect:
        print(0)
    else:
        print(1)
elif n == 2:
    line = find_line(*boom[0], *boom[1])
    ans = cnt(*boom[0], *boom[1])
    for x,y in protect:
        if line[0]*x + line[1]*y + line[2] == 0:
            if boom[0][0] <= x <= boom[1][0] and boom[0][1] <= y <= boom[1][1]:
                ans -= 1
            if boom[1][0] <= x <= boom[0][0] and boom[1][1] <= y <= boom[0][1]:
                ans -= 1
    print(ans)
else:    
    ch = convex_hull(boom)
    A = find_area(ch) # 넓이 
    b = -len(ch) # 변 위의 점
    for i in range(len(ch)):
        b += cnt(*ch[i], *ch[(i+1)%len(ch)])
    I = A - b//2 + 1 # 내부의 점
    
    ch2 = convex_hull2(boom)
    up = ch2[0]
    down = ch2[1]
    
    count = 0
    for point in protect:
        if is_in(point):
            count += 1
    
    print(b + I - count)