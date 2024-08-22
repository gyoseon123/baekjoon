import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(now, color):
    ret = True
    visited[now] = color
    for next in graph[now]:
        if visited[next] == -1:
            ret = ret & dfs(next, (color+1)%2)
        else:
            if visited[next] == visited[now]:
                return False
    
    return ret

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for i in range(1, n+1):
    graph[i].extend(list(map(int, input().split()))[1:])

for i in range(1, n+1):
    if visited[i] == -1:
        dfs(i, 0)

white = []
blue = []

for i in range(1, n+1):
    if visited[i] == 0: white.append(i)
    else: blue.append(i)

print(len(white))
print(*white)
print(len(blue))
print(*blue)

