import random
import sys
input = sys.stdin.readline

def is_line(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1) == 0

n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
visit = [False]*n

if n <= 4:
    print("success")
    exit()

# random.seed(123)
can = 0
for _ in range(10000):
    rnd = random.sample(range(n), 3)
    p1 = point[rnd[0]]
    p2 = point[rnd[1]]
    p3 = point[rnd[2]]
    if (is_line(*p1, *p2, *p3)):
        can = 1
        line1_p1 = p1
        line1_p2 = p2
        break

if not can:
    print("failure")
    exit()

other = []
for i in range(n):
    if (is_line(*line1_p1, *line1_p2, *point[i])): visit[i] = 1
    else: other.append((point[i], i))

if len(other) <= 2:
    print("success")
    exit()

line2_p1 = other[0][0]
line2_p2 = other[1][0]

for i in range(len(other)):
    if (is_line(*line2_p1, *line2_p2, *other[i][0])): visit[other[i][1]] = 1

if sum(visit) == n: print("success")
else: print("failure")