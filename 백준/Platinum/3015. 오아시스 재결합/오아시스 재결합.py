from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)] + [-1]

stk = []
ans = 0
cnt = Counter(l)
arr = []

c = 1
for i in range(n):
    if l[i] != l[i+1]:
        arr.append([l[i], c])
        c = 1
    else:
        c += 1

for i in range(len(arr)):
    now = arr[i]
    ans += now[1] * (now[1] - 1) // 2
    
    while stk and stk[-1][0] < now[0]:
        ans += stk[-1][1]
        stk.pop()

    tmp = 0
    while stk and stk[-1][0] == now[0]:
        ans += stk[-1][1] * now[1]
        tmp += stk[-1][1]
        stk.pop()
    
    if stk:
        ans += now[1]
    
    now[1] += tmp

    stk.append(now)  

print(ans)