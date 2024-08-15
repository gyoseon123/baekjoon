import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b,c,p = map(int, input().split())
    if a*b*c%p == 0:
        cnt = 0
        for num in (a,b,c):
            if num%p == 0:
                cnt += 1
        if cnt >= 2:
            print(1)
        else:
            print(0)
    else:
        print(0)