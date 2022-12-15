import sys
from collections import deque
t = int(sys.stdin.readline())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    while m != -1:
        if q[0] == max(q):
            q.popleft()
            m -= 1
            cnt += 1
        else:
            q.rotate(-1)
            if m == 0:
                m += len(q)-1
            else:
                m -= 1
    print(cnt)
    
            
