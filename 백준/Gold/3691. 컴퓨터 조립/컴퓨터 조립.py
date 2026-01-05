from collections import defaultdict
import sys
input = sys.stdin.readline
inf = sys.maxsize

def check(x):
    ret = 0
    
    for i in range(len(l)):
        mn = inf
        for j in range(len(l[i])):
            p,q = l[i][j]
            if q >= x:
                mn = min(mn, p)
        ret += mn
    
    return ret <= b

t = int(input())

for _ in range(t):
    n,b = map(int, input().split())
    d = defaultdict(list)
    
    for i in range(n):
        typ, name, price, quality = input().split()
        price = int(price)
        quality = int(quality)
        d[typ].append((price, quality))
    
    l = []
    
    for key, val in d.items():
        l.append(sorted(val))
    
    left = 0
    right = 2*int(1e12)
    
    while left + 1 < right:
        mid = (left + right)//2
        
        if check(mid): left = mid
        else: right = mid
    
    print(left)