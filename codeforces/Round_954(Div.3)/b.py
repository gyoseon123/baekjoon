import sys
input = sys.stdin.readline

t = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(t):
    n,m = map(int, input().split())
    met = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            x = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if (0 <= nx < n) and (0 <= ny < m):
                    x.append(met[nx][ny])
            if met[i][j] > max(x):
                met[i][j] = max(x)
    for i in met:
        print(*i)
