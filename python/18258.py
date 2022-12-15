import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([])
for i in range(n):
    s = sys.stdin.readline().strip()
    if s.startswith('push'):
        q.append(int(s.split()[1]))
    if s == 'pop':
        if len(q) != 0:
            print(q.popleft(0))
        else:
            print(-1)
    if s == 'size':
        print(len(q))
    if s == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if s == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    if s == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
