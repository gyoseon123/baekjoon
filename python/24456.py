n,m,k = map(int, input().split())

def divisor(n):
    result = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            result.append((i,n//i))
    return result
choco = n*m
cnt = 0
while choco > 1:
    choco -= 1
    div = divisor(choco)
    if abs(div[-1][0] - div[-1][1]) <= k:
        if len(div) == 1:
            cnt += choco
            break
        cnt += 1
    else:
        break
print(cnt)