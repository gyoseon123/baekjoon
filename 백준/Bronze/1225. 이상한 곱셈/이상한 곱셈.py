a,b = input().split()

n,m = 0,0

for i in range(len(a)):
    n += ord(a[i]) - ord('0')
    
for i in range(len(b)):
    m += ord(b[i]) - ord('0')
    
print(n*m)