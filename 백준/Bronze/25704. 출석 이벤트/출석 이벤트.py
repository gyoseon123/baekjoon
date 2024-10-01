n = int(input())
p = int(input())

if n >= 20:
    print(max(0, min(p - p//4, p - 2000)))
elif n >= 15:
    print(max(0, min(p - 2000, p - p//10)))
elif n >= 10:
    print(max(0, min(p - p//10, p - 500)))
elif n >= 5:
    print(max(0, p - 500))
else:
    print(p)