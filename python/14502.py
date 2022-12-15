import itertools
import sys
import copy
def dfs(x,y):
    if graph[x][y] == 2:
        for i in range(4):
            d_x = x + dx[i]
            d_y = y + dy[i]
            if d_x >= 0 and d_x < h and d_y >= 0 and d_y < w:
                if graph[d_x][d_y] == 0:
                    graph[d_x][d_y] = 2
                    dfs(d_x,d_y)

def count_safe(array):
    cnt = 0
    for o in array:
        for x in o:
            if x == 0:
                cnt += 1
    return cnt


dx = [1,0,-1,0]
dy = [0,1,0,-1]
h,w = map(int, sys.stdin.readline().split())
n_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
zero_lndex = []
result = []
for i in range(h):
    for j, s in enumerate(n_graph[i]):
        if s == 0:
            zero_lndex.append([i,j])


for i in itertools.combinations(zero_lndex,3):
    graph = copy.deepcopy(n_graph)
    for j in range(3):
        graph[i[j][0]][i[j][1]] = 1
    for a in range(h):
        for b in range(w):
            dfs(a,b)
    result.append(count_safe(graph))
print(max(result))