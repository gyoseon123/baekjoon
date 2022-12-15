n,m = map(int, input().split())
str = {}
for i in range(n):
    a,b = input().split()
    str[a] = b
for i in range(m):
    print(str[input()])