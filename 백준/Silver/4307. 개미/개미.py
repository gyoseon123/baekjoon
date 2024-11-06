import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l,n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    min_val = -int(1e9)
    max_val = -int(1e9)
    
    for i in range(n):
        min_val = max(min_val, min(abs(l - a[i]), a[i]))
        max_val = max(max_val, max(abs(l - a[i]), a[i]))
    
    print(min_val, max_val)