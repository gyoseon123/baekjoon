import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, int(n**0.5)*2+1):
        if n >= (i*(i+1))//2:
            if i&1 and n%i == 0: cnt += 1
            if not i&1 and n%i == i//2: cnt += 1
    print(cnt)