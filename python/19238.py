from collections import deque
import sys
input = sys.stdin.readline
n,m,fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
taxi = list(map(int, input().split()))
taxi[0] -= 1
taxi[1] -= 1
destination = {}

for _ in range(m):
    a,b,c,d = map(int, input().split())
    graph[a-1][b-1] = 2
    destination[(a-1,b-1)] = (c-1,d-1)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_people():
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((taxi[0], taxi[1], 0))
    visited[taxi[0]][taxi[1]] = True
    result = []
    if graph[taxi[0]][taxi[1]] == 2:
        graph[taxi[0]][taxi[1]] = 0
        return (0,taxi[0],taxi[1])

    while q:
        x,y,dis = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 2:
                    result.append((dis+1, nx, ny))
                q.append((nx,ny,dis+1))
    result.sort()
    if not result:
        return False
    graph[result[0][1]][result[0][2]] = 0
    return result[0]


def find_des(goal_x, goal_y):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((taxi[0], taxi[1], 0))
    visited[taxi[0]][taxi[1]] = True
    while q:
        x,y,dis = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if nx == goal_x and ny == goal_y:
                    return dis+1
                q.append((nx,ny,dis+1))


success = True
for _ in range(m):
    people = find_people()
    if not people:
        success = False
        break
    taxi = (people[1], people[2])
    fuel -= people[0]
    if fuel <= 0:
        success = False
        break
    move = find_des(destination[taxi][0], destination[taxi][1])
    if not move:
        success = False
        break
    fuel -= move
    if fuel < 0:
        success = False
        break
    taxi = (destination[taxi][0], destination[taxi][1])
    fuel += move*2

if success:
    print(fuel)
else:
    print(-1)
