from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

l = [tuple(map(int, input().split())) for _ in range(n)]

l.sort(key = lambda x : x[1])

arr = [0]

ans = 0

if n == 2:
    ans = l[1][1] - l[0][1]

for i,j in l:
    if i == 1: arr.append(i)
    else: arr.append(-1)
    
for i in range(n):
    arr[i+1] += arr[i]

d = defaultdict(int)

for i in range(1, n+1):
    now = arr[i]
    
    if d[now]:
        ans = max(ans, l[i-1][1] - l[d[now]][1])
    else:
        d[now] = i

print(ans)