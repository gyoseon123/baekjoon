# from collections import deque      3차원 배열 풀이
# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# graph = [[] for _ in range(n)]
# for i in range(n):
#     l = list(input().rstrip())
#     for j in l:
#         graph[i].append([j,j])

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# def bfs():
#     q = deque()
#     visited = [[[False,False] for _ in range(m)] for _ in range(n)]
#     q.append((0,0,0,1))
#     visited[0][0][0] = True
#     while q:
#         x,y,is_break,dis = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >= 0 and nx < n and ny >= 0 and ny < m:
#                 if is_break == 0:
#                     if graph[nx][ny][0] == '1' and not visited[nx][ny][1]:
#                         visited[nx][ny][1] = True
#                         q.append((nx,ny,1,dis+1))
#                     if graph[nx][ny][0] == '0' and not visited[nx][ny][0]:
#                         visited[nx][ny][0] = True
#                         q.append((nx,ny,0,dis+1))
#                 else:
#                     if not visited[nx][ny][1] and graph[nx][ny][1] == '0':
#                         visited[nx][ny][1] = True
#                         q.append((nx,ny,1,dis+1))
#         if x == n-1 and y == m-1:
#             return dis

# result = bfs()
# if result:
#     print(result)
# else:
#     print(-1)        

from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q = deque()
    visited = [[[False,False] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    q.append((0,0,1))
    while q:
        x,y,dis = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[x][y][1] == False: #벽 안부숨
                    if graph[nx][ny] == '0' and not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        q.append((nx,ny,dis+1))
                    if graph[nx][ny] == '1' and not visited[nx][ny][1]:
                        visited[nx][ny][0] = True
                        visited[nx][ny][1] = True
                        q.append((nx,ny,dis+1))
                else: #벽 부숨
                    if graph[nx][ny] == '0' and not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        visited[nx][ny][1] = True
                        q.append((nx,ny,dis+1))
        if x == n-1 and y == m-1:
            print(dis)
            return

                    
result = bfs()
print(result if result else -1)
    