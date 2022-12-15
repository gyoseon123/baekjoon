import sys
input = sys.stdin.readline
n,m = map(int, input().split())
if m > n-1:
    m = n-1
town = [list(map(int, input().split())) for _ in range(n)]
result = []
plus_dx = [i for i in range(1,m+1)] + [i for i in range(-m,0)] + [0]*(m*2)
plus_dy = [0]*(m*2) + [i for i in range(1,m+1)] + [i for i in range(-m,0)]
multiple_dx = [i for i in range(1,m+1)]*2 + [i for i in range(-1,-m-1,-1)]*2
multiple_dy = ([i for i in range(1,m+1)] + [i for i in range(-1,-m-1,-1)])*2


def plus_type(x,y):
    num = 0
    for i in range(len(plus_dx)):
        nx = x + plus_dx[i]
        ny = y + plus_dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            num += town[nx][ny]
    return num + town[x][y]


def multiple_type(x,y):
    num = 0
    for i in range(len(multiple_dx)):
        nx = x + multiple_dx[i]
        ny = y + multiple_dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            num += town[nx][ny]
    return num + town[x][y]

result = 0
for i in range(n):
    for j in range(n):
        k = max(plus_type(i,j), multiple_type(i,j))
        if k > result:
            result = k

print(result)