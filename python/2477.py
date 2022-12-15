from collections import deque
import sys
iuput = sys.stdin.readline
shape_1 = [4,2,3,1,3,1]
shape_2 = [4,2,4,2,3,1]
shape_3 = [4,2,3,2,3,1]
shape_4 = [4,2,3,1,4,1]

k = int(input())
shape = deque()
num = deque()
for i in range(6):
    a,b = map(int, input().split())
    shape.append(a)
    num.append(b)
result = 0
while True:
    s = list(shape)
    if s == shape_1:
        result = num[0]*num[1] - num[3]*num[4]
        break
    if s == shape_2:
        result = num[4]*num[5] - num[1]*num[2]
        break
    if s == shape_3:
        result = num[0]*num[5] - num[2]*num[3]
        break
    if s == shape_4:
        result = num[1]*num[2] - num[4]*num[5]
        break
    shape.rotate(1)
    num.rotate(1)
print(result*k)
    
