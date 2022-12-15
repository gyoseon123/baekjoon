import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]  * (n+1)
tree = [0]*(n+1)
for i in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            tree[i] = x
            dfs(i)
dfs(1)
tree = tree[2::]
for i in tree:
    print(i)