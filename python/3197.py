from collections import deque
import sys
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
r,c = map(int, input().split())
lake = [[] for _ in range(r)]
visited = [[False]*c for _ in range(r)]
water = []
next_water = []
swan = []
next_swan = []
q = deque()

for i in range(r):
    l = list(input())
    for j in range(c):
        if l[j] == '.':
            water.append((i,j))
        if l[j] == 'L':
            water.append((i,j))
            swan.append((i,j))
        lake[i].append(l[j])
swan1 = (swan[0][0], swan[0][1]) #백조 1
swan2 = (swan[1][0], swan[1][1]) #백조 2
lake[swan1[0]][swan1[1]], lake[swan2[0]][swan2[1]] = '.', '.' #백조를 물로 생각하고 탐색
q.append(swan1)
visited[swan1[0]][swan1[1]] = True
def melt():
    while water:
        x,y = water.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c and lake[nx][ny] == 'X':
                lake[nx][ny] = '.'
                next_water.append((nx,ny))

def find_swan():  # 1번 백조가 2번백조 탐색.
    global sig   
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if lake[nx][ny] == '.':
                    q.append((nx,ny))
                    if nx == swan2[0] and ny == swan2[1]:  # 2번백조를 발견했다면 return
                        sig = True
                        return
                else:
                    next_swan.append((nx,ny))  # X를 발견했다면 다음 탐색할곳에 추가
sig = False
cnt = 0
while True:
    melt()
    while next_water:
        water.append(next_water.pop())
    find_swan()
    while next_swan:
        q.append(next_swan.pop())
    cnt += 1
    if sig:
        print(cnt)
        break
