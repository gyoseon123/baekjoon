import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(0)
    exit()
    
tree = list(map(int, input().split()))
delete = int(input())
visited = [False]*n
graph = [[] for _ in range(n)]
for i in range(n):
    node = tree[i]
    if node == -1:
        root = i
        continue
    else:
        graph[node].append(i)

for l in graph:
    if delete in l:
        l.remove(delete)

cnt = 0
def dfs(v):
    global cnt
    visited[v] = True
    if len(graph[v]) == 0:
        cnt += 1
        return 
    for node in graph[v]:
        if not visited[node]:
            dfs(node)
if root == delete:
    print(0)
    exit()
dfs(root)
print(cnt)
    
