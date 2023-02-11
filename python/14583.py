import math
x,y = map(float, input().split())
a = (2*x*x-2*x*math.sqrt(x*x+y*y))/(-2*y)
W = math.sqrt(x*x+a*a)/2
H = ((y-a)*x)/(2*W)
print(f'{W:.2f} {H:.2f}')