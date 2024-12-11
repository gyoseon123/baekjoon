def p_list(n):
    p = [True]*(n+1)
    p[0], p[1] = 0,0
    
    for i in range(2, int(n**0.5)+1):
        if p[i]:
            for j in range(i*i, n+1, i):
                p[j] = False
    
    return p

n = int(input())
p = p_list(2000000)

while True:
    if not p[n]:
        n += 1
        continue
    if str(n) == str(n)[::-1]:
        print(n)
        break
    else:
        n += 1