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

l = int(input())
s = input()

pi = getpi(s)
print(l - pi[l-1])