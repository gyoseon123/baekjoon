import sys
input = sys.stdin.readline
mod = 1000

def matrix_multiple(matrix1,matrix2):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (matrix1[i][k]*matrix2[k][j])%mod
    return result

def solve(cnt):
    if cnt == 1:
        return matrix

    m = solve(cnt//2)
    if cnt&1:
        return matrix_multiple(matrix_multiple(m,m),matrix)
    else:
        return matrix_multiple(m,m)


n,b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = solve(b)
for i in range(n):
    for j in range(n):
        result[i][j] %= mod
for i in result:
    print(*i)
