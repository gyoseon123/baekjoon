import sys
import math
a, b = map(int, sys.stdin.readline().split())
def prime(x):
    if x == 1:
        return
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return 
    return x
for i in range(a,b+1):
    z = prime(i)
    if z != None:
        print(z)

import math
import time
def prime_num(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

# def prime(x):
#     if x == 1:
#         return False
#     for i in range(2,x-1):
#         if x%i == 0:
#             return False
#     return True

def prime_list(x):
    p = [True] * x
    for i in range(2,int(math.sqrt(x))+1):
        if p[i] == True:
            for j in range(i+i,x,i):
                p[j] = False
    return [i for i in range(2,x) if p[i] == True]







# s_time = time.time()
# # for i in range(1,1000001):
# #     if prime_num(i):
# #         print(i)
# print(prime_list(1000000))
# print(time.time() - s_time)

