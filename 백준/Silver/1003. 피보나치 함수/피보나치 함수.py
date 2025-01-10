n = int(input())
for j in range(n):
    f = [1,0]
    l = [0,1]
    a = int(input())
    for i in range(a):
        f[0],f[1] = f[0]+l[0], f[1]+l[1]
        f,l = l,f
    print(f[0],f[1], end = ' ')    