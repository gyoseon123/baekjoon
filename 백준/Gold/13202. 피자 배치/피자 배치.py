import sys
import math
input = sys.stdin.readline

PI = math.pi
t = int(input())

for _ in range(t):
    a,b,k = map(int, input().split())
    c = (a*a + b*b)**0.5
    r = (a + b - c)/2
    lines = [r]
    target = (((a - r)**2 + r**2)**0.5 - r)/(2*r)

    left = 0
    right = 1
    while True:
        mid = (left+right)/2
        if abs((mid / (1 - mid)) - target) < 1e-8:
            break

        if (mid / (1 - mid)) < target:
            left = mid
        else:
            right = mid
    
    exp = 1
    for i in range(100):
        lines.append(r * mid**exp)
        exp += 1
    
    
    target = ((r**2 + r**2)**0.5 - r)/(2*r)

    left = 0
    right = 1
    while True:
        mid = (left+right)/2
        if abs((mid / (1 - mid)) - target) < 1e-8:
            break

        if (mid / (1 - mid)) < target:
            left = mid
        else:
            right = mid
    
    exp = 1
    for i in range(100):
        lines.append(r * mid**exp)
        exp += 1
    
    
    target = (((b - r)**2 + r**2)**0.5 - r)/(2*r)

    left = 0
    right = 1
    while True:
        mid = (left+right)/2
        if abs((mid / (1 - mid)) - target) < 1e-8:
            break

        if (mid / (1 - mid)) < target:
            left = mid
        else:
            right = mid
    
    exp = 1
    for i in range(100):
        lines.append(r * mid**exp)
        exp += 1
    
    lines.sort(reverse=True)
    print(f"{lines[k-1]**2*PI:.8f}")
