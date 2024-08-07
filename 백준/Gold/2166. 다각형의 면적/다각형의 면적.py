import sys
input = sys.stdin.readline

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

n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
print(round(find_area(point)/2, 2))