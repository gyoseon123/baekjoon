n,p,q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0]*n

for i in range(n):
    ddal = a[i]
    sha = b[i]
    for j in range(10001):
        if ddal + p*j == sha + q*j:
            result[i] = j
            break
    else:
        print("NO")
        exit()
        
print("YES")
print(*result)