import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
k_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
def find(x,y,length): 
    visited[x][y] = True
    q = deque()
    q.append((x,y,length))
    while q:
        x,y,length = q.popleft()
        if x == n-1 and y == m-1:
            return length
        for i in range(1,k_map[x][y]+1):
            nx = x+i
            if nx < n and not visited[nx][y]:
                visited[nx][y] = True
                q.append((nx,y,length+1))
            ny = y+i
            if ny < m and not visited[x][ny]:
                visited[x][ny] = True
                q.append((x,ny,length+1))

print(find(0,0,0))
