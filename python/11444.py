mod = 1000000007

def square_matrix(matrix1,matrix2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (matrix1[i][k]*matrix2[k][j])%mod
    return result

def solve(cnt):
    if cnt == 1:
        return matrix

    m = solve(cnt//2)
    if cnt&1:
        return square_matrix(square_matrix(m,m),matrix)
    else:
        return square_matrix(m,m)
    

matrix = [[1,1],[1,0]]
n = int(input())
if n == 0 or n == 1:
    print(1)
    exit()

print(solve(n-1)[0][0]%mod)