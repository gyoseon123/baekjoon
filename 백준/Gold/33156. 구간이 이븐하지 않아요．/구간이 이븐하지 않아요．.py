from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n-1):
    l = i
    r = i+1
    diff = 0
    ld = defaultdict(int)
    rd = defaultdict(int)
    
    ld[a[l]] += 1
    rd[a[r]] += 1
    if (ld[a[l]] != rd[a[l]]): diff += 1
    if (ld[a[r]] != rd[a[r]]): diff += 1
    
    if diff == 0: ans = max(ans, 2)
    
    while True:
        l -= 1
        r += 1
        if (l < 0 or r >= n): break
        ld[a[l]] += 1
        rd[a[r]] += 1
        if (ld[a[l]] != rd[a[l]] and a[l] != a[r] and ld[a[l]]-1 == rd[a[l]]): diff += 1
        if (ld[a[r]] != rd[a[r]] and a[l] != a[r] and ld[a[r]] == rd[a[r]]-1): diff += 1
        if (ld[a[l]] == rd[a[l]] and a[l] != a[r]): diff -= 1
        if (ld[a[r]] == rd[a[r]] and a[l] != a[r]): diff -= 1
        if diff == 0:
            ans = max(ans, r - l + 1)

print(ans)