from math import *

def dist(x1, y1, z1, x2, y2, z2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())
x3, y3, z3 = map(int, input().split())

def are_collinear(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    V1 = (x2 - x1, y2 - y1, z2 - z1)
    V2 = (x3 - x1, y3 - y1, z3 - z1)

    cross_x = V1[1] * V2[2] - V1[2] * V2[1]
    cross_y = V1[2] * V2[0] - V1[0] * V2[2]
    cross_z = V1[0] * V2[1] - V1[1] * V2[0]

    return cross_x == 0 and cross_y == 0 and cross_z == 0

if are_collinear(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    d1 = dist(x1, y1, z1, x2, y2, z2)
    d2 = dist(x2, y2, z2, x3, y3, z3)
    d3 = dist(x1, y1, z1, x3, y3, z3)
    print(max(d1, d2, d3))
    exit()

d1_3 = (x3-x1)**2 + (y3-y1)**2 + (z3 - z1)**2
d1_2 = (x2-x1)**2 + (y2-y1)**2 + (z2 - z1)**2
d2_3 = (x3-x2)**2 + (y3-y2)**2 + (z3 - z2)**2

dot1 = (x3-x1)*(x2-x1) + (y3-y1)*(y2-y1) + (z3-z1)*(z2-z1)
dot2 = (x3-x2)*(x1-x2) + (y3-y2)*(y1-y2) + (z3-z2)*(z1-z2)
dot3 = (x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3)

cos_theta1 = ( dot1 ) / ((sqrt(d1_3)) * (sqrt(d1_2)))
sin_theta1= sqrt(1- cos_theta1**2)

if(degrees(acos(cos_theta1)) >= 120):
    print((sqrt(d1_3)) + (sqrt(d1_2)))
    exit(0)

cos_theta2 = ( dot2 ) / ((sqrt(d2_3)) * (sqrt(d1_2)))
sin_theta2= sqrt(1- cos_theta2**2)

if(degrees(acos(cos_theta2)) >= 120):
    print((sqrt(d2_3)) + (sqrt(d1_2)))
    exit(0)

cos_theta3 = ( dot3 ) / ((sqrt(d1_3)) * (sqrt(d2_3)))
sin_theta3= sqrt(1- cos_theta3**2)

if(degrees(acos(cos_theta3)) >= 120):
    print((sqrt(d1_3)) + (sqrt(d2_3)))
    exit(0)


a = sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
b = sqrt((x2 - x3)**2 + (y2 - y3)**2 + (z2 - z3)**2)
c = sqrt((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2)

s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
sin_ = (area * 2 / (a*c))

if(degrees(acos(cos_theta1)) >= 90):
    theta = pi - asin(sin_)
else:
    theta = asin(sin_)

l = sqrt(c**2 + a**2 - 2*c*a*cos(theta + pi/3))

print(l)