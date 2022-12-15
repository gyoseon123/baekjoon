from collections import deque
import sys
input = sys.stdin.readline
a,b = input().split()
q = deque()
q.append([a,1])
ans = -1
def bfs():
    global ans
    while q:
        x,y = q.popleft()
        if x == b:
            ans = y
            break
        if int(x)*2 <= int(b):
            q.append([str(int(x)*2), y+1])
        if int(x+'1') <= int(b):
            q.append([x + '1', y+1])

bfs()
print(ans)
