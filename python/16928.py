import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n,m = map(int, input().split())
board = [0] * 101
visited = [0] * 101
for i in range(n+m):
    x,y = map(int, input().split())
    board[x] = y
q.append(1)
visited[1] = 1
def bfs():
    while q:
        x = q.popleft()
        for i in range(1,7):
            nx = x+i
            if nx <= 100 :
                if board[nx] != 0:
                    nx = board[nx]
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
            if nx == 100:
                return visited[nx] - 1
print(bfs())