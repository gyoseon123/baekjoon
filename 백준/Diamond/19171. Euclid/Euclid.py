from math import *

x1, y1, z1 = map(int, input().split());
x2, y2, z2 = map(int, input().split());
x3, y3, z3 = map(int, input().split());

v1 = (x2 - x1, y2 - y1, z2 - z1)
v2 = (x3 - x1, y3 - y1, z3 - z1)

if v1[1] * v2[2] - v1[2] * v2[1] == 0 and v1[2] * v2[0] - v1[0] * v2[2] == 0 and v1[0] * v2[1] - v1[1] * v2[0] == 0:
    x_min = min(x1, x2, x3)
    x_max = max(x1, x2, x3)
    y_min = min(y1, y2, y3)
    y_max = max(y1, y2, y3)
    z_min = min(z1, z2, z3)
    z_max = max(z1, z2, z3)

    # print("line")
    print(sqrt((x_max - x_min) ** 2 + (y_max - y_min) ** 2 + (z_max - z_min) ** 2))
    exit(0)

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

l = sqrt(d1_2 + d2_3 - 2*sqrt(d1_2)*sqrt(d2_3)*(cos_theta2/2 - sin_theta2/2*sqrt(3)))

print(l)

