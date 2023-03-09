import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

if sum(arr)&1:
    print(-1)
    exit()

graph = [[0]*n for _ in range(n)]

edges = []
for i in range(n):
    edges.append([arr[i], i])
edges.sort(reverse=True)

while True:
    now = edges[0][1]
    if edges[0][0] == 0:
        break
    for i in range(1,n):
        node = edges[i][1]
        if graph[node][now] == 0:
            graph[node][now] = 1
            graph[now][node] = 1
            edges[0][0] -= 1
            edges[i][0] -= 1
            if edges[0][0] == 0:
                break
    edges.sort(reverse=True)
for l in graph:
    print(*l)