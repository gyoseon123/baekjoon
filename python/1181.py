a = int(input())
str = []
for i in range(a):
    str.append(input())
str = set(str)
str = list(str)
str.sort()
str.sort(key = len)
for i in str:
    print(i)
