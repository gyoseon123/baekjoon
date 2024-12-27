import sys
input = sys.stdin.readline
    
mod = int(1e9)+7

def square_matrix(matrix1,matrix2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (matrix1[i][k]%mod*matrix2[k][j]%mod)%mod
    return result

def solve(cnt):
    if cnt == 1:
        return matrix

    m = solve(cnt//2)
    if cnt&1:
        return square_matrix(square_matrix(m,m),matrix)
    else:
        return square_matrix(m,m)
    

matrix = [[4,-1],[1,0]]

n = int(input())
if n%2 == 1:
    print(0)
    exit()
elif n == 2:
    print(3)
    exit()
    
s = solve(n//2-1)
print((s[0][0]*3 + s[0][1]) %mod)