import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
def dfs(x):
    for node in range(n):
        if not visited[node] and graph[x][node] == 1:
            visited[node] = True
            dfs(node)


for i in range(n):
    visited = [False] * (n)
    dfs(i)
    for j in visited:
        if j == True:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()

