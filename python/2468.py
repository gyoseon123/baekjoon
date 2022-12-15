import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

max = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > max:
            max = graph[i][j]



def dfs(x,y,arr):
    arr[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and arr[nx][ny] == 1:
            arr[nx][ny] = 0
            dfs(nx,ny,arr)
            return True
    return False

result = []
for i in range(2,max):
    ori_graph = copy.deepcopy(graph)
    for a in range(n):
        for b in range(n):
            if graph[a][b] <= i:
                graph[a][b] = 1
            else:
                graph[a][b] = 0
    print(*graph, sep='\n')
    print()
    cnt = 0
    for a in range(n):
        for b in range(n):
            if dfs(a,b, graph):
                cnt += 1
    result.append(cnt)
    graph = copy.deepcopy(ori_graph)
print(result)
    

