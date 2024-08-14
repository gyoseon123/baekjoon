import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

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
        
    return abs(sumP - sumM)

def convex_hull(points):
    points.sort()
    stk1 = []
    stk2 = []
    for point in points:
        while len(stk1) >= 2:
            if ccw(*stk1[-2], *stk1[-1], *point) >= 0:
                stk1.pop()
            else:
                break
            
        while len(stk2) >= 2:
            if ccw(*stk2[-2], *stk2[-1], *point) <= 0:
                stk2.pop()
            else:
                break
        
        stk1.append(point)
        stk2.append(point)
        
    return stk1 + list(reversed(stk2[1:len(stk2)-1]))   

n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
ch = convex_hull(point)
print(find_area(ch)//100)