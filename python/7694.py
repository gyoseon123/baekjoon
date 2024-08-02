import sys
input = sys.stdin.readline

def gcd(a,b):
    if b != 0:
        return gcd(b, a%b)
    return a

def find_area():
    return abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1)/2

def cnt(px1, py1, px2, py2):
    dx = abs(px1 - px2)
    dy = abs(py1 - py2)
    return gcd(dx, dy) + 1

while True:
    l = list(map(int, input().split()))
    if l == [0,0,0,0,0,0]: break

    x1,y1,x2,y2,x3,y3 = l
    A = find_area()
    b = cnt(x1, y1, x2, y2) + cnt(x2, y2, x3, y3) + cnt(x3, y3, x1, y1) - 3

    print(int(A - b/2 + 1))