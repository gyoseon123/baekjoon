def gcd(a,b):
    if b != 0:
        return gcd(b, a%b)
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

x,y = map(int, input().split())
n = x*y

res = [int(1e9), -1, -1]

for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        a,b = i, n//i
        if i + n//i < res[0] and gcd(a,b) == x and lcm(a,b) == y:
            res = [i + n//i, i, n//i]
            
print(*res[1:])