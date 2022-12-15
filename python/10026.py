import sys
import copy
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
temp = copy.deepcopy(graph)


def dfs_red(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 'R':
        graph[x][y] = 0
        for i in range(4):
            dfs_red(x + dx[i], y + dy[i])
        return True
    return False

def dfs_blue(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 'B':
        graph[x][y] = 0
        for i in range(4):
            dfs_blue(x + dx[i], y + dy[i])
        return True
    return False

def dfs_green(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 'G':
        graph[x][y] = 0
        for i in range(4):
            dfs_green(x + dx[i], y + dy[i])
        return True
    return False

def dfs_green_or_red(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 'G' or graph[x][y] == 'R':
        graph[x][y] = 0
        for i in range(4):
            dfs_green_or_red(x + dx[i], y + dy[i])
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(n):
        if dfs_blue(i,j):
            cnt += 1
        if dfs_red(i,j):
            cnt += 1
        if dfs_green(i,j):
            cnt += 1
print(cnt, end = ' ')
cnt = 0
graph = temp
for i in range(n):
    for j in range(n):
        if dfs_blue(i,j):
            cnt += 1
        if dfs_green_or_red(i,j):
            cnt += 1
print(cnt)