def gcd(a,b):
    for i in range(2,a+1):
        if a%i == 0 and b%i == 0:
            x = i
    return x
a,b = map(int, input().split())
print(gcd(a,b))
print(int(a*b / gcd(a,b)))