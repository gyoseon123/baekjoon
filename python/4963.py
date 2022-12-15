import sys
sys.setrecursionlimit(1000000)
def dfs(x,y):
    if x <= -1 or x >= w or y <= -1 or y >= h:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x-1,y-1)
        dfs(x+1,y+1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        return True
    return False

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    cnt = 0
    for i in range(w):
        for j in range(h):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)


