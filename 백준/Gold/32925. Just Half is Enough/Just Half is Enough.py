import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    cnt = 0
    for i in range(m):
        u,v = map(int, input().split())
        if u < v: cnt += 1
    
    if cnt >= (m+1)//2:
        print(*[i for i in range(1, n+1)])
    else:
        print(*[i for i in range(n, 0, -1)])
    
    