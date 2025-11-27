a,b = 0,1
c = list()
for i in range(91):
    c.append(a)
    a,b = b, a+b
l = int(input())
print(c[l])