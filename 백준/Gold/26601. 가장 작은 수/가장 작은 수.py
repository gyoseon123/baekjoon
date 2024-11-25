MAX = 1515151

def p_list(n):
    p = [True]*(n+1)
    p[0], p[1] = False, False
    
    for i in range(2, int(n**0.5)+1):
        if p[i]:
            for j in range(i*i, n+1, i):
                p[j] = False
    
    return p

sq = [False]*MAX
p = p_list(MAX)

for i in range(1, int(MAX**0.5)+1):
    if p[i]:
        for j in range(100):
            if i**(1 << j) < MAX:
                sq[i**(1 << j)] = True
            else:
                break

n = int(input())

ans = 1
cnt = 0
mod = 2000003

for i in range(2, MAX):
    if cnt == n:
        break
    
    if p[i] or sq[i]:
        ans = (ans * i)%mod
        cnt += 1
        
print(ans)