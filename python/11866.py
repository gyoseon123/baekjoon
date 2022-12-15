import sys
from collections import deque
a,b = map(int, sys.stdin.readline().split())
q = deque([])
for i in range(1,a+1):
    q.append(i)
print('<', end = '')
while len(q) != 0:
    q.rotate(-b+1)
    print(q.popleft(), end = '')
    if len(q) != 0:
        print(', ', end = '')
print('>')