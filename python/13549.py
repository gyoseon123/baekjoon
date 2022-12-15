import sys
from collections import deque
from time import time
input = sys.stdin.readline
n,k = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append([n,0])
def bfs():
    while q:
        global ans
        x,time = q.popleft()
        if visited[x] == 1:
            continue
        if x == k:
            return time
        if x*2 < 100001:
            q.append([x*2, time])
        if x-1 >= 0 and x-1 < 100001:
            q.append([x-1, time+1])
        if x+1 < 100001:
            q.append([x+1, time+1])
        visited[x] = 1
print(bfs())