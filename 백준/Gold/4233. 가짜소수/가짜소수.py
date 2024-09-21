import sys
input = sys.stdin.readline

def is_p(n):
    if n == 1: return False

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    
    return True

while True:
    p,a = map(int, input().split())
    if (p,a) == (0,0): break
    
    if not is_p(p) and pow(a, p, p) == a:
        print("yes")
    else:
        print("no")