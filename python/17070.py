n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0]]*(n+1) for _ in range(n+1)] # 가로, 세로, 대각선
dp[1][1] = [0,0,0]
dp[1][2] = [1,0,0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dp[i+1][j+1] = [-1,0,0]

sig = 0
for i in range(n): # 세로
    for j in range(n): # 가로
        if dp[i+1][j+1][0] == -1:
            continue
        if i == 0 and j == 1:
            continue    

        if dp[i][j+1][0] == -1:
            sig = 1 # 위에가 막힘
        elif dp[i+1][j][0] == -1:
            sig = 2 # 왼쪽이 막힘
        elif dp[i][j][0] == -1:
            sig = 3 # 왼쪽대각 막힘
        else:
            sig = 0

        if sig == 1:
            dp[i+1][j+1] = [dp[i+1][j][0] + dp[i+1][j][2], 0, 0]
        elif sig == 2:
            dp[i+1][j+1] = [0,dp[i][j+1][1] + dp[i][j+1][2], 0]
        elif sig == 3:
            dp[i+1][j+1] = [dp[i+1][j][0] + dp[i+1][j][2], dp[i][j+1][1] + dp[i][j+1][2], 0]
        else:
            dp[i+1][j+1] = [dp[i+1][j][0] + dp[i+1][j][2], dp[i][j+1][1] + dp[i][j+1][2], sum(dp[i][j])]


x = sum(dp[n][n])
if x == -1:
    print(0)
else:
    print(x)

# dfs 풀이

# import sys
# import copy
# input = sys.stdin.readline
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# graph[0][0], graph[0][1] = 1,1
# dx = [0,1,1]
# dy = [1,0,1]
# cnt = 0
# def dfs(x,y, graph, state):
#     global cnt
#     if x == n-1 and y == n-1:
#         cnt += 1
#         return
#     for i in range(3):
#         if state == 'garo' and i == 1:
#             continue
#         if state == 'sero' and i == 0:
#             continue
#         new_graph = copy.deepcopy(graph)
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < n and ny < n:
#             if i == 2:
#                 if graph[nx][ny] == 0 and graph[nx-1][ny] == 0 and graph[nx][ny-1] == 0:
#                     new_graph[nx][ny] = 1
#                     dfs(nx,ny, new_graph, 'degak')
#             else:
#                 if graph[nx][ny] == 0:
#                     new_graph[nx][ny] = 1
#                     if i == 0:
#                         dfs(nx,ny,new_graph, 'garo')
#                     else:
#                         dfs(nx,ny,new_graph, 'sero')

# dfs(0,1, graph, 'garo')
# print(cnt)

