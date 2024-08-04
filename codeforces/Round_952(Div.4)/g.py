import sys
input = sys.stdin.readline

t = int(input())

def digits_sum(n):
    ret = 0
    while n > 0:
        ret += n%10
        n //= 10
    return ret


for _ in range(t):
    # l,r,k = map(int, input().split())

    l = 0
    r = 4
    for k in range(10, 300):
        for i in range(10**l, 10**r):
            if digits_sum(k*i) == k*digits_sum(i):
                print(i)
    
    print("!!")
