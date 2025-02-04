def metrix_multiple(metrix1, metrix2):
    metrix3 = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                metrix3[i][j] += (metrix1[i][k] * metrix2[k][j])%mod

    return metrix3

def solve(n):
    if n == 1:
        return init_metrix
    
    ret = solve(n//2)
    if n&1:
        return metrix_multiple(init_metrix, metrix_multiple(ret, ret))
    else:
        return metrix_multiple(ret, ret)


mod = int(1e9)+7
n,m = map(int, input().split())

if n < m:
    print(1)
    exit()
elif n == m:
    print(2)
    exit()

init_metrix = [[0]*m for _ in range(m)]
init_metrix[0][0] = 1
init_metrix[0][m-1] = 1

for i in range(m-1):
    init_metrix[i+1][i] = 1
    
res = solve(n-m+1)
print(sum(res[0])%mod)


