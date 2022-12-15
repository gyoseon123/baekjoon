n = int(input())
l = [list(map(int,list(input()))) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
def dfs(x,y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if l[x][y] == 1:
        l[x][y] = 0
        count += 1
        for i in range(4):
            dfs(x+dx[i],y+dy[i])

result = []
for i in range(n):
    for j in range(n):
        dfs(i,j)
        if count != 0:
            result.append(count)
result = list(dict.fromkeys(result))
for i in range(len(result)-1,0,-1):
    result[i] -= result[i-1]
result.sort()
print(len(result))
for i in result:
    print(i)

        