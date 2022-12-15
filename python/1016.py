import math
import sys
import time
input = sys.stdin.readline
a,b = map(int, input().split())
n = time.time()
prime = [True] * (int(math.sqrt(b))+1)
num = [True] * (b-a+1)
for i in range(2,int(math.sqrt(b))):
    if prime[i] == True:
        for j in range(i*2, int(math.sqrt(b))+1, i):
            prime[j] = False
prime[0], prime[1] = False, False
for i in range(len(prime)):
    if prime[i] == True:
        x = i**2
        for j in range(-a%x,b-a+1,x):
            if j >= 0:
                num[j] = 0
print(num.count(True))
print(time.time() - n)
