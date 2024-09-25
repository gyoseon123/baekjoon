from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    global ans, flg
    visited[x][y] = True
    if board[x][y] == "$":
        ans += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < h) and (0 <= ny < w) and not visited[nx][ny]:
            next = board[nx][ny]
            if next == "." or next == "$":
                dfs(nx,ny)
            elif next in ual:
                if chr(ord(next) + ord("a") - ord("A")) in key:
                    dfs(nx,ny)
                else:
                    door.append((nx,ny))
            elif next in lal:
                if next not in key:
                    flg = True
                key.add(next)
                dfs(nx,ny)
            
        
    

t = int(input())
ual = set([chr(i) for i in range(ord("A"), ord("Z")+1)])
lal = set([chr(i) for i in range(ord("a"), ord("z")+1)])


for _ in range(t):
    h,w = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    ans = 0
    k = input().rstrip()
    key = set()
    door = deque()
    
    if k != '0':
        key = set(list(k))
    
    for i in range(h):
        for j in range(w):
            if i in (0, h-1) or j in (0, w-1):
                if not visited[i][j]:
                    now = board[i][j]
                    if now == "." or now == "$":
                        dfs(i,j)
                    elif now in ual:
                        if chr(ord(now) + ord("a") - ord("A")) in key:
                            dfs(i,j)
                        else:
                            door.append((i,j))
                    elif now in lal:
                        key.add(now)
                        dfs(i,j)
    
    visit = [False]*10101
    while True:
        flg = False
        for i in range(len(door)):
            if visit[i]:
                continue
            x,y = door[i]
            now = board[x][y]
            if chr(ord(now) + ord("a") - ord("A")) in key:
                visit[i] = True
                dfs(x,y)
        if not flg:
            break

    print(ans)
    