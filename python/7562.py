import sys
from collections import deque
input = sys.stdin.readline
dx = [2,2,1,1,-1,-1,-2,-2]
dy = [1,-1,2,-2,2,-2,1,-1]
t = int(input())


def knight(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < l and ny >= 0 and ny < l and not visited[nx][ny]:
                chess[nx][ny] = chess[x][y] + 1
                visited[nx][ny] = True
                if nx == goal_x and ny == goal_y:
                    return 
                q.append([nx,ny])

for i in range(t):
    l = int(input())
    chess = [[0] * (l) for _ in range(l)]
    visited = [[False] * (l) for _ in range(l)]
    now_x, now_y= map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    knight(now_x, now_y)
    print(chess[goal_x][goal_y])
