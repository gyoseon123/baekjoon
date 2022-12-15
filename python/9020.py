import sys
import math
n = int(sys.stdin.readline())
def prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return
    return True
for i in range(n):
    a = int(sys.stdin.readline())
    a //= 2
    x = 0
    while True:
        q,w = a-x, a+x
        if prime(q) and prime(w):
            print(q,w)
            break
        x += 1
        
        



