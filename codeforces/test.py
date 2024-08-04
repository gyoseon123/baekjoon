def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n&i == 0:
            return False
    
    return True

l = [-1]*200001

for i in range(1, 200001):
    if l[i] == -1:
        l[i] = i
    
    for j in range(i+1, 200001):
        if is_prime(i^j):
            l[j] = l[i]

print(l)
