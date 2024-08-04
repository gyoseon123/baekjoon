import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    s = list(input().rstrip())
    ind = list(map(int, input().split()))
    c = list(input().rstrip())
    ind.sort()
    c.sort()
    cnt = 0
    arr = sorted(set(ind))
    for i in range(len(arr)):
        s[arr[i]-1] = c[i]
    
    print(''.join(s))

