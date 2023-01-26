# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# cnt = 0
# def dfs(x,y):
#     global cnt
#     if x == n-1 and y == m-1:
#         cnt += 1
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] < graph[x][y]:
#             dfs(nx,ny)

# dfs(0,0)
# print(cnt)
    
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = list(map(int, input().split()) for _ in range(n))
dp = [[0]*m for _ in range(n)]

