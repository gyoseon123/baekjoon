from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[a] += 1
    indegree[b] += 1
q = deque()
more_three_edge = 0
for i in range(n+1):
    if indegree[i] >= 3:
        more_three_edge += 1

if more_three_edge == 0:
    print(*[i for i in range(n)])

erase = []
for i in range(n+1):
    if indegree[i] == 1:
        erase.append(i)
        indegree[i] = 0
q.append(erase)
visited = [False]*(n+1)
while q:
    node_list = q.popleft()
    next_erase = []
    for node in node_list:
        visited[node] = True
    for node in node_list:
        for next in graph[node]:
            if indegree[next] == 3:
                more_three_edge -= 1
                if more_three_edge == 0:
                    break
            indegree[next] -= 1
            if indegree[next] == 1:
                indegree[next] = 0
                next_erase.append(next)
        else:
            continue
        break
    else:
        q.append(next_erase)
        continue
    break

for i in range(n):
    if not visited[i]:
        print(i, end=' ')