from collections import deque

N,M,V = map(int,input().split())
visited = [0]*(N+1)
visited_2 = visited.copy()
#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1,N+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited_2[v] = 1
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1,N+1):
            if visited_2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_2[i] = 1

                
dfs(V)
print()
bfs(V)



