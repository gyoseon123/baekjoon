# import sys
# input = sys.stdin.readline
# r,c = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# result = 0

# cnt = 0
# def dfs(x,y,dis):
#     print(x,y)
#     global result
#     global cnt
#     cnt += 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         result = max(result, dis)
#         if nx >= 0 and nx < r and ny >= 0 and ny < c:
#             if not visited[ord(graph[nx][ny])-65]:
#                 visited[ord(graph[nx][ny])-65] = True
#                 dfs(nx,ny,dis+1)
#                 visited[ord(graph[nx][ny])-65] = False
# visited = [False]*26
# visited[ord(graph[0][0])-65] = True
# dfs(0,0,1)
# print(result)
# print(cnt)



import sys
input = sys.stdin.readline
r,c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
result = 0
check = [[0]*c for _ in range(r)]
cnt = 0
def dfs(x,y,dis,visited):
    print(x,y)
    global result
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        result = max(result, dis)
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if visited & 1 << (ord(graph[nx][ny])-64) == 0:
                temp = visited | (1 << (ord(graph[nx][ny])-64))
                if check[nx][ny] != temp:
                    check[nx][ny] = temp
                    dfs(nx,ny,dis+1,temp)
                
dfs(0,0,1,1<<(ord(graph[0][0])-64))
print(result)
print(cnt)