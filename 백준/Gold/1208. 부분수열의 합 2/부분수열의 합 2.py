from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline

def find(target):
    left = 0
    right = len(sec)-1
    while left + 1 < right:
        mid = (left + right)//2
        if sec[mid] >= target:
            right = mid
        else:
            left = mid
    
    if sec[right] == target:
        return True
    else:
        return False

n,s = map(int, input().split())
l = list(map(int, input().split()))

left = l[:n//2]
right = l[n//2:]

fir = []
sec = set()
cnt = defaultdict(int)

for i in range(len(left)+1):
    for arr in combinations(left, i):
        fir.append(sum(arr))

for i in range(1, len(right)+1):
    for arr in combinations(right, i):
        ss = sum(arr)
        cnt[ss] += 1
        sec.add(ss)

ans = 0
if s == 0:
    ans -= 1

for i in range(len(fir)):
    if fir[i] == s:
        ans += 1

    if s - fir[i] in sec:
        ans += cnt[s-fir[i]]

print(ans)