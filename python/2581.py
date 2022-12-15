a = int(input())
b = int(input())

prime_num = []
num = [i for i in range(b+1)]
for i in range(2,b+1):
    for j in range(a,b+1):
        if num[j] != i:
            if num[j]%i == 0:
                num[j] = 0
for i in num:
    if i > a and i != 0 and i != 1:
        prime_num.append(i)
if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))