import sys
from collections import deque
import itertools
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
result = []
check = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()


for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i,j])
            graph[i][j] = 0

def bfs(arr):
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
                if [nx,ny] in arr:
                    pass
                else:
                    cnt += 1
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx,ny])
    if cnt == 0:
        return True
def find_max(array):
    max = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] > max:
                max = array[i][j]
    return max

def check_zero(array):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                cnt += 1
    return cnt


temp = copy.deepcopy(graph)

for i in itertools.combinations(virus, m):
    comp = []
    for j in i:
        q.append(j)
        comp.append(j)
    if bfs(comp) == True:
        result.append(0)
        graph = copy.deepcopy(temp)
        continue
    if check_zero(graph) == m:
        result.append(find_max(graph))
    graph = copy.deepcopy(temp)

if len(result) == 0:
    print(-1)
else:
    print(min(result))



