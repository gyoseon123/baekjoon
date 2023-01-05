def square_area(x1,y1,x2,y2,x3,y3,x4,y4):
    left = x1*y2 + x2*y3 + x3*y4 + x4*y1
    right = x2*y1 + x3*y2 + x4*y3 + x1*y4
    return abs(left-right)*0.5

def tri_area(x1,y1,x2,y2,x3,y3):
    left = x1*y2 + x2*y3 + x3*y1
    right = x2*y1 + x3*y2 + x1*y3
    return abs(left-right)*0.5

x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
