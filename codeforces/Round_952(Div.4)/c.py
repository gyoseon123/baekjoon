import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    if n == 1:
        if arr[0] == 0:
            print(1)
            continue
        else:
            print(0)
            continue

    s = arr[0]
    if arr[0] == 0:
        ans = 1
    else:
        ans = 0

    before_max = arr[0]
    for i in range(1,n):
        now = arr[i]
        if now == s or before_max == s - before_max + now:
            ans += 1
        if before_max < now:
            before_max = now
        s += now
    print(ans)
        

    