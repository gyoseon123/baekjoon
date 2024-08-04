import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    
    s = l[-1]
    e = l[-1] + k
    for i in range(n-1):
        num = l[i]
        v = (num + ((e - num)//(2*k))*2*k)

        s = max(s, v)
        e = min(e, v+k)
    
    if s >= e:
        print(-1)
    else:
        print(s)


    