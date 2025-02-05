from collections import defaultdict
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    
    ans = 0
    cnt = 0
    for i in range(n):
        now = x^a[i]
        if now == a[i]:
            if d[now] >= 2:
                ans += d[now]-1
        else:
            if now in d:
                ans += d[now]
                
    print(ans//2)
                