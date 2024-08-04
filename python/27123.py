def gcd(a,b):
    if b != 0:
        return gcd(b, a%b)
    return a


def cnt(px1, py1, px2, py2):
    dx = abs(px1 - px2)
    dy = abs(py1 - py2)
    if dy > dx:
        dx,dy = dy,dx

    return gcd(dx, dy) + 1


dirx = [1,1,0,-1,-1,-1,0,1]
diry = [0,1,1,1,0,-1,-1,-1]
while True:
    numX = []
    numY = []
    sumP, sumM = 0,0
    sp, sm = 0,0

    try:
        s = input()
    except:
        break


    for i in range(len(s)):
        x,y = dirx[int(s[i])], diry[int(s[i])]
        sp += x
        sm += y
        numX.append(sp)
        numY.append(sm)
    numX.append(numX[0])
    numY.append(numY[0])
    for i in range(len(s)):
        sumP += numX[i]*numY[i+1]
        sumM += numX[-i-1]*numY[-i-2]
    A = abs(sumP-sumM)/2
    b = -len(s)
    for i in range(len(s)-1):
        b += cnt(numX[i], numY[i], numX[i+1], numY[i+1])
    b += cnt(numX[0], numY[0], numX[len(s)-1], numY[len(s)-1])
    
    print(int(A - b/2 + 1) + b)
       