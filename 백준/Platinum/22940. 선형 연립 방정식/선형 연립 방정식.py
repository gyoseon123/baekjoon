import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

mat.sort(key=lambda x : [-abs(x[i]) for i in range(n)])

for i in range(n):
    now = mat[i][i]
    if now == 0:
        print("No unique solution")
        exit()
        
    for j in range(i+1, n):
        diff = mat[j][i]/now
        for k in range(i, n+1):
            mat[j][k] -= mat[i][k] * diff

for i in range(n):
    if mat[i][i] == 0:
        print("No unique solution")
        exit()
    diff = 1/mat[i][i]
    for j in range(n+1):
        mat[i][j] *= diff

for i in range(n-1, -1, -1):
    now = mat[i][i]
    if now == 0:
        print("No unique solution")
        exit()
    for j in range(i-1, -1, -1):
        diff = mat[j][i]/now
        for k in range(n+1):
            mat[j][k] -= mat[i][k] * diff

ans = []
for i in range(n):
    now = mat[i][n]
    ans.append(now)

eps = 1e-6
for i in range(n):
    print(f"{ans[i]:.0f}", end=' ')