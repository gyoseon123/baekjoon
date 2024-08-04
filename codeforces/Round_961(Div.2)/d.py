import math
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    flg = False
    for i in range(n):
        if l[i] == 0:
            if s != n:
                print(-1)
                flg = True
                break
    if flg:
        continue

    ans = 0
    arr = []
    arr.append((l[0], 1))
    for i in range(1, n):
        a = arr[-1][0]
        x1 = arr[-1][1]
        b = l[i]
        x2 = math.ceil(x1*math.log(a,2)/math.log(b,2))
        arr.append((l[i], x2))
        ans += math.ceil((math.log(x2,2)))
    print(ans)