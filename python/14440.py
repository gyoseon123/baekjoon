MOD = 100

def multiple_matrix(matrix1, matrix2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (matrix1[i][k]*matrix2[k][j])%MOD
    return result

def power_matrix(cnt):
    if cnt == 1:
        return matrix
    
    m = power_matrix(cnt//2)
    if cnt&1:
        return multiple_matrix(multiple_matrix(m,m),matrix)
    else:
        return multiple_matrix(m,m)

x,y,a0,a1,n = map(int, input().split())

if n == 0:
    if len(str(a0)) == 1:
        print('0' + str(a0))
    else:
        print(a0)
    exit()
if n == 1:
    if len(str(a1)) == 1:
        print('0' + str(a1))
    else:
        print(a1)
    exit()
    
matrix = [[x,y],[1,0]]
r = power_matrix(n-1)
result = (r[0][0]*a1 + r[0][1]*a0)%MOD
if len(str(result)) == 1:
    print('0' + str(result))
else:
    print(result)

