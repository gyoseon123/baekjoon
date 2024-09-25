from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def make_wall(x1, y1, x2, y2):
    if x1 == x2:
        if y2 < y1:
            y1,y2 = y2,y1
            
        for i in range(y1-1, y2):
            board[x1-1][i] = -1
    elif y1 == y2:
        if x2 < x1:
            x1,x2 = x2,x1
            
        for i in range(x1-1, x2):
            board[i][y1-1] = -1
    else:
        p1 = (x1, y1)
        p2 = (x2, y2)
        if p1[0] > p2[0]:
            p1,p2 = p2,p1
        
        if p1[1] > p2[1]:
            for i in range(p2[0] - p1[0] + 1):
                board[p1[0] + i - 1][p1[1] - i - 1] = -1
        else:
            for i in range(p2[0] - p1[0] + 1):
                board[p1[0] + i - 1][p1[1] + i - 1] = -1

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy,1))
    visited = [[False]*Y for _ in range(X)]
    while q:
        x,y,c = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < X) and (0 <= ny < Y) and board[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny] = 1
                if c+1 < t:
                    q.append((nx,ny,c+1))
        
while True:
    try:
        X,Y,t,l,w = map(int, input().split())
    except: break
    board = [[0]*Y for _ in range(X)]
    
    loc = []
    arr = []
    cnt = 0
    while True:
        pos = list(map(int, input().split()))
        arr.extend(pos)
        cnt += len(pos)
        if cnt == 2*l: break
    
    for i in range(0, 2*l, 2): loc.append((arr[i], arr[i+1]))
    
    if w > 0:
        cnt = 0
        arr = []
        while True:
            wall = list(map(int, input().split()))
            arr.extend(wall)
            cnt += len(wall)
            if cnt == w*4: break
        for i in range(0, w*4, 4):
            make_wall(*arr[i:i+4])
    
    for x,y in loc:
        board[x-1][y-1] = 1
        bfs(x-1, y-1)
    
    ans = 0
    for i in range(X):
        for j in range(Y):
            if board[i][j] == 1:
                ans += 1
    
    print(ans)