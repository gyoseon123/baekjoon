import sys
input = sys.stdin.readline
sys.setrecursionlimit(200001)

def solve(now, col):
    global ans
    visited[now] = True
    if col != color[now-1]:
        ans += 1
    
    for next in graph[now]:
        if not visited[next]:
            solve(next, color[now-1])


n = int(input())
color = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
ans = 0
visited = [False]*(n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)  
    graph[b].append(a)  

solve(1, 0)

print(ans)