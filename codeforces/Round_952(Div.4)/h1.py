
# import sys
# input = sys.stdin.readline

# t = int(input())
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def dfs(x,y,cnt,dep):
#     visited[x][y] = True
#     component[x][y] = cnt
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < n) and (0 <= ny < m):
#             if not visited[nx][ny] and board[nx][ny] == "#":
#                 dfs(nx,ny,cnt,dep+1)


# for _ in range(t):
#     n,m = map(int, input().split())
#     board = [input().rstrip() for _ in range(n)]
#     component = [[-1]*m for _ in range(n)]
#     value = [0]*(int(1e6))
#     visited = [[False]*m for _ in range(n)]
#     comp = 1
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == "#" and not visited[i][j]:
#                 dfs(i,j,comp,1)
#                 comp += 1 
    
#     for i in range(n):
#         for j in range(m):
#             if component[i][j] != -1:
#                 value[component[i][j]] += 1

#     ans = 0

#     for i in range(n):
#         val = 0
#         used = set()
#         for j in range(m):

#             if component[i][j] == -1:
#                 val += 1
#             else:
#                 if component[i][j] not in used:
#                     val += value[component[i][j]]
#                     used.add(component[i][j])

#             if i+1 < n:
#                 if component[i+1][j] != -1 and component[i+1][j] not in used:
#                     val += value[component[i+1][j]]
#                     used.add(component[i+1][j])
            
#             if i-1 >= 0:
#                 if component[i-1][j] != -1 and component[i-1][j] not in used:
#                     val += value[component[i-1][j]]
#                     used.add(component[i-1][j])
        
#         ans = max(ans, val)
    
#     for i in range(m):
#         val = 0
#         used = set()
#         for j in range(n):

#             if component[j][i] == -1:
#                 val += 1
#             else:
#                 if component[j][i] not in used:
#                     val += value[component[j][i]]
#                     used.add(component[j][i])

#             if i+1 < m:
#                 if component[j][i+1] != -1 and component[j][i+1] not in used:
#                     val += value[component[j][i+1]]
#                     used.add(component[j][i+1])
            
#             if i-1 >= 0:
#                 if component[j][i-1] != -1 and component[j][i-1] not in used:
#                     val += value[component[j][i-1]]
#                     used.add(component[j][i-1])

#         ans = max(ans, val)
    
#     print(ans)




