from collections import deque
n,k = map(int, input().split())

tracking = [0]*200001

def bfs(v):
    q = deque()
    q.append(v)
    visited = [False]*200001
    visited[v] = True
    while q:
        v = q.popleft()
        if v+1 <= 200000 and not visited[v+1]:
            visited[v+1] = True
            tracking[v+1] = v
            q.append(v+1)
        if v-1 >= 0 and not visited[v-1]:
            visited[v-1] = True
            tracking[v-1] = v
            q.append(v-1)
        if v*2 <= 200000 and not visited[v*2]:
            visited[v*2] = True
            tracking[v*2] = v
            q.append(v*2)

bfs(n)
tmp = k
cnt = 0
result = []
while k != n:
    result.append(k)
    k = tracking[k]
    cnt += 1
print(cnt)
print(n,*list(reversed(result)))