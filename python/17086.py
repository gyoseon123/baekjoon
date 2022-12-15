# from collections import deque    빈칸에 대해서 전부 탐색
# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dx = [1,1,1,0,0,-1,-1,-1]
# dy = [1,0,-1,1,-1,1,-1,0]


# def bfs(x,y):
#     visited[x][y] = True
#     q = deque()
#     q.append((x,y,1))
#     while q:
#         x,y,depth = q.popleft()
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
#                 if graph[nx][ny] == 1:
#                     result.append(depth)
#                     return
#                 visited[nx][ny] = True
#                 q.append((nx,ny,depth+1))
# result = []
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             visited = [[False]*m for _ in range(n)]
#             bfs(i,j)

# print(max(result))
                
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,-1,0]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))
            visited[i][j] = True
while q:
    x,y = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny))
result = max(map(max, graph))
print(result-1)