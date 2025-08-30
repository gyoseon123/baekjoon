n,k = map(int, input().split())

div = []

x = 2
while k > 1:
    while (k%x == 0):
        div.append(x)
        k //= x
    x += 1

flg = 1
for num in div:
    if num%2 == 0: flg = 0

if (k == 2):
    for i in range(n):
        for j in range(n):
            if (i&1)^(j&1): print(1, end=' ')
            else: print(0,end=' ')
        print()
else:
    if not flg: print(-1)
    else:
        for i in range(n):
            for j in range(n):
                print(1, end=' ')
            print()