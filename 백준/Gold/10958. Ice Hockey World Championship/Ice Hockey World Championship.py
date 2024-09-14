from itertools import combinations
import bisect
import sys
input = sys.stdin.readline



n,m = map(int, input().split())
l = list(map(int, input().split()))

arr1 = []
arr2 = []
for i in range(n//2):
    arr1.append(l[i])
for i in range(n//2, n):
    arr2.append(l[i])

cnt = {}
comb1 = set()
comb2 = []

for i in range(len(arr1)+1):
    for l in combinations(arr1, i):
        s = sum(l)
        if s <= m:
            try:
                cnt[s] += 1
            except:
                cnt[s] = 1
        comb1.add(s)
            

for i in range(len(arr2)+1):
    for l in combinations(arr2, i):
        s = sum(l)
        comb2.append(s)

comb2.sort()
comb1 = list(comb1)

ans = 0
for num in comb1:
    target = m - num
    if target >= 0:
        count = bisect.bisect_right(comb2, target)
        ans += count*cnt[num]

print(ans)
