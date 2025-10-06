import random
import sys
input = sys.stdin.readline

def is_line(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0

n = int(input())
p = int(input())

if n == 1:
    print("possible")
    exit()

point = [list(map(int, input().split())) for _ in range(n)]

most = 0
for _ in range(300):
    p1, p2 = random.sample(point, 2)
    cnt = 0
    for i in range(n):
        if is_line(*p1, *p2, *point[i]): cnt += 1
    most = max(most, cnt)

print("possible" if most * 100 >= p * n else "impossible")