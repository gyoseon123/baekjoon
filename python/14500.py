import sys
input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
type_2_shape = (((1,0),(-1,0),(0,0),(0,1)),((1,0),(-1,0),(0,0),(0,-1)),
((-1,0),(0,-1),(0,0),(0,1)),((1,0),(0,-1),(0,0),(0,1)))

result = []
def type_1(x,y,length,csum,visited):
    if length == 4:
        result.append(csum+board[x][y])
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if (nx,ny) not in visited:
                type_1(nx,ny,length+1,csum+board[x][y],visited|{(x,y)})

def type_2(x,y):
    l = []
    for i in type_2_shape:
        sig = True
        csum = 0
        for j in i:
            nx = x + j[0]
            ny = y + j[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                sig = False
            else:
                csum += board[nx][ny]
        if sig:
            l.append(csum)
    if l:
        return max(l)
    else:
        return 0
                
max_result = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if cnt&1 == 0:
            result = []
            type_1(i,j,1,0,set())
            k = max(max(result), type_2(i,j))
            if k > max_result:
                max_result = k
        cnt += 1
print(max_result)




