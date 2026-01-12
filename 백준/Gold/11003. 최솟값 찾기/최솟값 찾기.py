from collections import deque
import sys
input = sys.stdin.readline

n,l = map(int, input().split())
a = list(map(int, input().split()))
q = deque()

for i,num in enumerate(a):
    while q and q[-1][0] >= num:
        q.pop()
    q.append((num, i))
    while q and i - q[0][1] >= l:
        q.popleft()
    
    print(q[0][0], end=' ')