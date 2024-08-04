import sys
input = sys.stdin.readline

def gcd(a,b):
    if b != 0:
        return gcd(b, a%b)
    return a

def cnt(px1, py1, px2, py2):
    dx = abs(px1 - px2)
    dy = abs(py1 - py2)
    return gcd(dx, dy) + 1

n = int(input())
numX = []
numY = []
sumP, sumM =0,0
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    numX.append(x)
    numY.append(y)
numX.append(numX[0])
numY.append(numY[0])
for i in range(n):
    sumP += numX[i]*numY[i+1]
    sumM += numX[-i-1]*numY[-i-2]
A = abs(sumP-sumM)/2
b = -n
for i in range(n-1):
    b += cnt(numX[i], numY[i], numX[i+1], numY[i+1])
b += cnt(numX[0], numY[0], numX[n-1], numY[n-1])

print(int(A - b/2 + 1))

   