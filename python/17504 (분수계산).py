def gcd(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def plus_fraction(d1,u1,d2,u2):
    d = d1*d2
    u = u1*d2+u2*d1
    gcd_du = gcd(d,u)
    d //= gcd_du
    u //= gcd_du
    return (d,u)

n = int(input())
num = list(map(int, input().split()))
num.reverse()

x = (1,num[0])
for i in range(1,n):
    x = plus_fraction(1,num[i],x[1],x[0])
print(x[1]-x[0],x[1])
    
