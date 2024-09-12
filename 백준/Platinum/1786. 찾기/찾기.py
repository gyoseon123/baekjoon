def getpi(s):
    m = len(s)
    pi = [0]*m
    j = 0
    
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    
    return pi

t = input()
p = input()
pi = getpi(p)
ans = []

n = len(t)
m = len(p)
j = 0

for i in range(n):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]
    
    if t[i] == p[j]:
        j += 1
        if j == len(p):
            ans.append(i-m+2)
            j = pi[j-1]

print(len(ans))
print(*ans)