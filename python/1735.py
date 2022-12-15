import sys
input = sys.stdin.readline
n1,n2 = map(int, input().split())
n3,n4 = map(int, input().split())

def gcd(a,b):
    while b!= 0:
        r = a%b
        a = b
        b = r
    return a



if n1 != 1 and n2 != 1:
    k = gcd(n1,n2)
    n2//= k
    n1//= k

if n3 != 1 and n4 != 1:   
    k = gcd(n3,n4)
    n4//= k
    n3//= k


x = n2*n4//gcd(n2,n4)
a = x//n4*n3+x//n2*n1
if x != 1 and a != 1: 
    k = gcd(x,a)
    x//= k
    a//= k

print(a, x)