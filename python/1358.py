import sys
from math import sqrt, pow
input = sys.stdin.readline
w,h,x,y,p = map(int, input().split())

def in_ground(nx,ny):
    if nx >= x and ny >= y and nx <= x+w and ny <= y+h:
        return True
    elif sqrt(pow(nx-x,2) + pow(ny-(y+h/2),2)) <= h/2:
        return True
    elif sqrt(pow(nx-(x+w),2) + pow(ny-(y+h/2),2)) <= h/2:
        return True
    else:
        return False

cnt = 0
for i in range(p):
    p_x, p_y = map(int, input().split())
    if in_ground(p_x,p_y):
        cnt += 1
print(cnt)