from collections import deque
import sys
input = sys.stdin.readline
n,m,s,t = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v,w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

def bfs(start,end):
    visited = [False]*(n+1)
    q = deque()
    q.append((start,0))
    visited[start] = True
    while q:
        node, dis = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                if next == end:
                    return dis+1
                visited[next] = True
                q.append((next, dis+1))

def find_dis(s):
    distance = [0]*n
    visited = [False]*(n+1)
    q = deque()
    q.append((s,0))
    visited[s] = True
    distance[0] += 1
    while q:
        node, dis = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                distance[dis+1] += 1
                q.append((next,dis+1))
    return distance
min_dis = bfs(s,t)-2
start_dis = find_dis(s)
end_dis = find_dis(t)
ans = 0
for i in range(min_dis+1):
    ans += start_dis[i] * end_dis[min_dis-i]
print(ans)