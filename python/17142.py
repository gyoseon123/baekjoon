import copy
from collections import deque
from itertools import combinations as cb
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

blank = 0
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))
            graph[i][j] = 0
        elif graph[i][j] == 0:
            blank += 1
check = set(virus)

graph_cp = copy.deepcopy(graph)

ans = int(1e9)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for case in cb(virus, m):
    graph = copy.deepcopy(graph_cp)
    q = deque()
    visited = [[False]*n for _ in range(n)]
    
    for x,y in case:
        graph[x][y] = 2
        visited[x][y] = True
        q.append((x,y))
    cnt = 0
    while q:
        if cnt == blank:
            val = max(map(max, graph))
            ans = min(ans, val-2)

        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                if (nx,ny) not in check:
                    cnt += 1


print(ans if ans != int(1e9) else -1)
    


    
