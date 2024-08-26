import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)
    dir1 = ccw(*p1, *p2, *p3)*ccw(*p1, *p2, *p4)
    dir2 = ccw(*p3, *p4, *p1)*ccw(*p3, *p4, *p2)
    
    if (dir1, dir2) == (0,0):
        if p2 > p1:
            p1, p2 = p2, p1
        if p4 > p3:
            p3, p4 = p4, p3
        
        return (p3 <= p2 and p1 <= p4) or (p2 <= p3 and p4 <= p1)
    
    return dir1 <= 0 and dir2 <= 0

def dfs(now):
    visited[now] = True
    ret = 1

    for next in graph[now]:
        if not visited[next]:
            ret += dfs(next)
    
    return ret

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
visited = [False]*n

for i in range(n):
    for j in range(i+1, n):
        if is_cross(*points[i], *points[j]):
            graph[i].append(j)
            graph[j].append(i)

cnt = 0
ans = -1
for i in range(n):
    if not visited[i]:
        cnt += 1
        ans = max(ans, dfs(i))

print(cnt)
print(ans)

