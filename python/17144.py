import copy
import sys
input = sys.stdin.readline
r,c,t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
air_clear = []
for i in range(r):
    if room[i][0] == -1:
        air_clear.append(i)

def spread(graph):
    new_graph = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            locate = graph[i][j]
            if locate == -1:
                new_graph[i][j] = -1
            if locate > 0:
                spread_dust = locate//5
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < r and ny >= 0 and ny < c and graph[nx][ny] != -1:
                        new_graph[nx][ny] += spread_dust
                        cnt += 1
                new_graph[i][j] += locate - (spread_dust)*cnt
    return new_graph

def rotate(graph):
    new_graph = copy.deepcopy(graph)
    up = air_clear[0]
    down = air_clear[1]
    
    for i in range(1,c-1): # 왼 -> 오
        new_graph[up][i+1] = graph[up][i]
        new_graph[down][i+1] = graph[down][i]
    new_graph[up][1] = 0
    new_graph[down][1] = 0
    for i in range(1,c): # 오 -> 왼
        new_graph[r-1][i-1] = graph[r-1][i]
        new_graph[0][i-1] = graph[0][i]
    for i in range(1,up+1): # 위쪽 아래 -> 위
        new_graph[i-1][c-1] = graph[i][c-1]
    for i in range(down,r-1): #아래쪽 위 -> 아래
        new_graph[i+1][c-1] = graph[i][c-1]
    new_graph[up-1][0] = 0
    new_graph[down+1][0] = 0
    for i in range(down+2,r): # 아래쪽 아래 -> 위
        new_graph[i-1][0] = graph[i][0]
    for i in range(0,up-1):
        new_graph[i+1][0] = graph[i][0]
    return new_graph

def sum_list(graph):
    cnt = 0
    for i in range(r):
        for j in range(c):
            x = graph[i][j]
            if x != -1:
                cnt += x
    return cnt



for i in range(t):
    room = spread(room)
    room = rotate(room)
print(sum_list(room))
